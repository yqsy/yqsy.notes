---
title: grin
date: 2018-08-09 11:51:23
categories: [项目分析]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. cuckoo](#2-cuckoo)

<!-- /TOC -->




<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
git clone https://github.com/mimblewimble/grin

.                    52087 
./core               11054  # 核心cuckoo-cycle算法,区块定义
./wallet             8588 
./servers            6928 
./chain              5789 
./p2p                3900 
./src                3748 
./store              3308 
./api                2770 
./keychain           2082 
./pool               1829 
./util               1086 
./config             1005 
./.idea              0 
./.hooks             0 
./.git               0 
./doc                0 
```


<a id="markdown-2-cuckoo" name="2-cuckoo"></a>
# 2. cuckoo


测试用例
```rust
#[cfg(test)]
mod test {
	use super::*;
	use pow::types::PoWContext;

	#[test]
	fn lean_miner() {
		let nonce = 15465723;
		let header = [0u8; 84].to_vec(); // with nonce
		let edge_bits = 19;

        // 1. 输入数据 1) nonce 2) header 3) edge_bits
		let mut lean = Lean::new(edge_bits);
		lean.set_header_nonce(header.clone(), nonce);

        // 2. trim掉不存在cycle的边
		lean.trim();

        // 3. 生成图 1) edge_bits 2) proof_size  3) max_sols
		let mut ctx_u32 = CuckatooContext::<u32>::new_impl(edge_bits, 42, 10).unwrap();

        // 4. 寻找环
		ctx_u32.set_header_nonce(header, Some(nonce), true).unwrap();
		lean.find_cycles(ctx_u32).unwrap();
	}
}

```

基础数据结构以及流程
```rust
pub struct Lean {
	params: CuckooParams<u32>,
	edges: Bitmap,
}

pub struct CuckooParams<T>
where
	T: EdgeType,
{
	pub edge_bits: u8,           // 边的左移距离,决定内存大小
	pub proof_size: usize,       // 寻找目标环的cycle数量
	pub num_edges: u64,          // 左移后的数量
	pub siphash_keys: [u64; 4],  // 对header + nonce 进行blake2b,输出的4个8字节的siphash_keys
	pub edge_mask: T,            // ?
}

pub struct CuckatooContext<T>
where
	T: EdgeType,
{
	params: CuckooParams<T>,
	graph: Graph<T>,
}

struct Graph<T>
where
	T: EdgeType,
{
	/// Maximum number of edges
	max_edges: T,
	/// Maximum nodes
	max_nodes: u64,
	/// Adjacency links
	links: Vec<Link<T>>,
	/// Index into links array
	adj_list: Vec<T>,
	///
	visited: Bitmap,
	/// Maximum solutions
	max_sols: u32,
	///
	pub solutions: Vec<Proof>,
	/// proof size
	proof_size: usize,
	/// define NIL type
	nil: T,
}

```

生成siphash_keys
```rust
// 输入header + nonce , 输出到 siphash_keys 4个8字节数字
pub fn set_header_nonce(&mut self, header: Vec<u8>, nonce: u32) {
    self.params.reset_header_nonce(header, Some(nonce)).unwrap();
}

Lean::set_header_nonce -> CuckooParams::reset_header_nonce -> set_header_nonce -> create_siphash_keys -> blake2b
```

寻找cycle
```rust

Lean::find_cycles -> CuckatooContext::find_cycles_iter 
```

挖矿
```rust

main -> server_command -> start_server -> start_server_tui -> Server::start -> start_stratum_server -> run_loop 

// 创建区块
mine_block::get_block -> build_block

// 计算难题
inner_mining_loop -> create_pow_context -> CuckatooContext::<T>::new -> CuckatooContext::<T>::new_impl

PoWContext<T>::set_header_nonce

PoWContext<T>::find_cycles
```

接口
```rust

pub struct BlockHeader {
	/// Version of the block
	pub version: u16,
	/// Height of this block since the genesis block (height 0)
	pub height: u64,
	/// Hash of the block previous to this in the chain.
	pub previous: Hash,
	/// Root hash of the header MMR at the previous header.
	pub prev_root: Hash,
	/// Timestamp at which the block was built.
	pub timestamp: DateTime<Utc>,
	/// Merklish root of all the commitments in the TxHashSet
	pub output_root: Hash,
	/// Merklish root of all range proofs in the TxHashSet
	pub range_proof_root: Hash,
	/// Merklish root of all transaction kernels in the TxHashSet
	pub kernel_root: Hash,
	/// Total accumulated sum of kernel offsets since genesis block.
	/// We can derive the kernel offset sum for *this* block from
	/// the total kernel offset of the previous block header.
	pub total_kernel_offset: BlindingFactor,
	/// Total size of the output MMR after applying this block
	pub output_mmr_size: u64,
	/// Total size of the kernel MMR after applying this block
	pub kernel_mmr_size: u64,
	/// Proof of work and related
	pub pow: ProofOfWork,
}

pub struct ProofOfWork {
	/// Total accumulated difficulty since genesis block
	pub total_difficulty: Difficulty,
	/// Difficulty scaling factor between the different proofs of work
	pub scaling_difficulty: u32,
	/// Nonce increment used to mine this block.
	pub nonce: u64,
	/// Proof of work data.
	pub proof: Proof,
}

pub struct Difficulty {
	num: u64,
}

pub struct Proof {
	/// Power of 2 used for the size of the cuckoo graph
	pub edge_bits: u8,
	/// The nonces
	pub nonces: Vec<u64>,
}


```

难度调整

```rust
/// Default Cuckoo Cycle edge_bits, used for mining and validating.
pub const DEFAULT_MIN_EDGE_BITS: u8 = 30;

/// Secondary proof-of-work edge_bits, meant to be ASIC resistant.
pub const SECOND_POW_EDGE_BITS: u8 = 29;

 
EDGE_BITS 29
proof_diff = scaling_difficulty << 64 / Proof::hash().to_u64()

EDGE_BITS 30 或其他 (!=29)   3840??
proof_diff = (2 << (proof.edge_bits - global::base_edge_bits())) * proof.edge_bits

if proof_diff >= (新块.pow.total_difficulty - 上一块.pow.total_difficulty) {
	出块成功
}

```
