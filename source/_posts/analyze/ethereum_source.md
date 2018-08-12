---
title: ethereum_source
date: 2018-08-12 15:26:03
categories: [项目分析]
---


<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->



# 1. 说明

```bash
.
├── accounts
│   ├── abi
│   │   ├── abi.go
│   │   ├── abi_test.go
│   │   ├── argument.go
│   │   ├── bind
│   │   │   ├── auth.go
│   │   │   ├── backend.go
│   │   │   ├── backends
│   │   │   │   └── simulated.go
│   │   │   ├── base.go
│   │   │   ├── bind.go
│   │   │   ├── bind_test.go
│   │   │   ├── template.go
│   │   │   ├── topics.go
│   │   │   ├── util.go
│   │   │   └── util_test.go
│   │   ├── doc.go
│   │   ├── error.go
│   │   ├── event.go
│   │   ├── event_test.go
│   │   ├── method.go
│   │   ├── numbers.go
│   │   ├── numbers_test.go
│   │   ├── pack.go
│   │   ├── pack_test.go
│   │   ├── reflect.go
│   │   ├── type.go
│   │   ├── type_test.go
│   │   ├── unpack.go
│   │   └── unpack_test.go
│   ├── accounts.go
│   ├── errors.go
│   ├── hd.go
│   ├── hd_test.go
│   ├── keystore
│   │   ├── account_cache.go
│   │   ├── account_cache_test.go
│   │   ├── file_cache.go
│   │   ├── key.go
│   │   ├── keystore.go
│   │   ├── keystore_passphrase.go
│   │   ├── keystore_passphrase_test.go
│   │   ├── keystore_plain.go
│   │   ├── keystore_plain_test.go
│   │   ├── keystore_test.go
│   │   ├── keystore_wallet.go
│   │   ├── presale.go
│   │   ├── testdata
│   │   │   ├── dupes
│   │   │   ├── keystore
│   │   │   │   └── foo
│   │   │   └── v1
│   │   │       └── cb61d5a9c4896fb9658090b597ef0e7be6f7b67e
│   │   ├── watch_fallback.go
│   │   └── watch.go
│   ├── manager.go
│   ├── url.go
│   ├── url_test.go
│   └── usbwallet
│       ├── hub.go
│       ├── internal
│       │   └── trezor
│       │       ├── messages.pb.go
│       │       ├── trezor.go
│       │       └── types.pb.go
│       ├── ledger.go
│       ├── trezor.go
│       └── wallet.go
├── build
│   ├── ci.go
│   ├── deb
│   │   ├── ethereum
│   │   └── ethereum-swarm
│   └── update-license.go
├── cmd
│   ├── abigen
│   │   └── main.go
│   ├── bootnode
│   │   └── main.go
│   ├── clef
│   │   ├── docs
│   │   │   └── qubes
│   │   └── main.go
│   ├── ethkey
│   │   ├── changepassphrase.go
│   │   ├── generate.go
│   │   ├── inspect.go
│   │   ├── main.go
│   │   ├── message.go
│   │   ├── message_test.go
│   │   ├── run_test.go
│   │   └── utils.go
│   ├── evm
│   │   ├── compiler.go
│   │   ├── disasm.go
│   │   ├── internal
│   │   │   └── compiler
│   │   │       └── compiler.go
│   │   ├── json_logger.go
│   │   ├── main.go
│   │   ├── runner.go
│   │   └── staterunner.go
│   ├── faucet
│   │   ├── faucet.go
│   │   └── website.go
│   ├── geth
│   │   ├── accountcmd.go
│   │   ├── accountcmd_test.go
│   │   ├── bugcmd.go
│   │   ├── chaincmd.go
│   │   ├── config.go
│   │   ├── consolecmd.go
│   │   ├── consolecmd_test.go
│   │   ├── dao_test.go
│   │   ├── genesis_test.go
│   │   ├── main.go
│   │   ├── misccmd.go
│   │   ├── monitorcmd.go
│   │   ├── run_test.go
│   │   ├── testdata
│   │   └── usage.go
│   ├── internal
│   │   └── browser
│   │       └── browser.go
│   ├── p2psim
│   │   └── main.go
│   ├── puppeth
│   │   ├── genesis.go
│   │   ├── module_dashboard.go
│   │   ├── module_ethstats.go
│   │   ├── module_explorer.go
│   │   ├── module_faucet.go
│   │   ├── module.go
│   │   ├── module_nginx.go
│   │   ├── module_node.go
│   │   ├── module_wallet.go
│   │   ├── puppeth.go
│   │   ├── ssh.go
│   │   ├── wizard_dashboard.go
│   │   ├── wizard_ethstats.go
│   │   ├── wizard_explorer.go
│   │   ├── wizard_faucet.go
│   │   ├── wizard_genesis.go
│   │   ├── wizard.go
│   │   ├── wizard_intro.go
│   │   ├── wizard_netstats.go
│   │   ├── wizard_network.go
│   │   ├── wizard_nginx.go
│   │   ├── wizard_node.go
│   │   └── wizard_wallet.go
│   ├── rlpdump
│   │   └── main.go
│   ├── swarm
│   │   ├── config.go
│   │   ├── config_test.go
│   │   ├── db.go
│   │   ├── download.go
│   │   ├── export_test.go
│   │   ├── fs.go
│   │   ├── fs_test.go
│   │   ├── hash.go
│   │   ├── list.go
│   │   ├── main.go
│   │   ├── manifest.go
│   │   ├── manifest_test.go
│   │   ├── mru.go
│   │   ├── run_test.go
│   │   ├── swarm-smoke
│   │   │   ├── main.go
│   │   │   └── upload_and_sync.go
│   │   ├── upload.go
│   │   └── upload_test.go
│   ├── utils
│   │   ├── cmd.go
│   │   ├── customflags.go
│   │   ├── customflags_test.go
│   │   └── flags.go
│   └── wnode
│       └── main.go
├── common
│   ├── big.go
│   ├── bitutil
│   │   ├── bitutil.go
│   │   ├── bitutil_test.go
│   │   ├── compress_fuzz.go
│   │   ├── compress.go
│   │   └── compress_test.go
│   ├── bytes.go
│   ├── bytes_test.go
│   ├── compiler
│   │   ├── solidity.go
│   │   └── solidity_test.go
│   ├── debug.go
│   ├── fdlimit
│   │   ├── fdlimit_freebsd.go
│   │   ├── fdlimit_test.go
│   │   ├── fdlimit_unix.go
│   │   └── fdlimit_windows.go
│   ├── format.go
│   ├── hexutil
│   │   ├── hexutil.go
│   │   ├── hexutil_test.go
│   │   ├── json_example_test.go
│   │   ├── json.go
│   │   └── json_test.go
│   ├── main_test.go
│   ├── math
│   │   ├── big.go
│   │   ├── big_test.go
│   │   ├── integer.go
│   │   └── integer_test.go
│   ├── mclock
│   │   └── mclock.go
│   ├── path.go
│   ├── size.go
│   ├── size_test.go
│   ├── test_utils.go
│   ├── types.go
│   └── types_test.go
├── consensus
│   ├── clique
│   │   ├── api.go
│   │   ├── clique.go
│   │   ├── snapshot.go
│   │   └── snapshot_test.go
│   ├── consensus.go
│   ├── errors.go
│   ├── ethash
│   │   ├── algorithm.go
│   │   ├── algorithm_test.go
│   │   ├── api.go
│   │   ├── consensus.go     # 难度重新计算
│   │   ├── consensus_test.go
│   │   ├── ethash.go
│   │   ├── ethash_test.go
│   │   └── sealer.go       # 挖矿
│   └── misc
│       ├── dao.go
│       └── forks.go
├── console
│   ├── bridge.go
│   ├── console.go
│   ├── console_test.go
│   ├── prompter.go
│   └── testdata
├── containers
│   └── docker
│       ├── develop-alpine
│       ├── develop-ubuntu
│       ├── master-alpine
│       └── master-ubuntu
├── contracts
│   ├── chequebook
│   │   ├── api.go
│   │   ├── cheque.go
│   │   ├── cheque_test.go
│   │   ├── contract
│   │   │   ├── chequebook.go
│   │   │   └── code.go
│   │   └── gencode.go
│   └── ens
│       ├── contract
│       │   ├── ens.go
│       │   ├── fifsregistrar.go
│       │   └── publicresolver.go
│       ├── ens.go
│       └── ens_test.go
├── core
│   ├── asm
│   │   ├── asm.go
│   │   ├── asm_test.go
│   │   ├── compiler.go
│   │   ├── lexer.go
│   │   └── lex_test.go
│   ├── bench_test.go
│   ├── blockchain.go
│   ├── blockchain_test.go
│   ├── blocks.go
│   ├── block_validator.go
│   ├── block_validator_test.go
│   ├── bloombits
│   │   ├── doc.go
│   │   ├── generator.go
│   │   ├── generator_test.go
│   │   ├── matcher.go
│   │   ├── matcher_test.go
│   │   ├── scheduler.go
│   │   └── scheduler_test.go
│   ├── chain_indexer.go
│   ├── chain_indexer_test.go
│   ├── chain_makers.go
│   ├── chain_makers_test.go
│   ├── dao_test.go
│   ├── error.go
│   ├── events.go
│   ├── evm.go
│   ├── gaspool.go
│   ├── genesis_alloc.go
│   ├── genesis.go
│   ├── genesis_test.go
│   ├── gen_genesis_account.go
│   ├── gen_genesis.go
│   ├── headerchain.go
│   ├── helper_test.go
│   ├── mkalloc.go
│   ├── rawdb
│   │   ├── accessors_chain.go
│   │   ├── accessors_chain_test.go
│   │   ├── accessors_indexes.go
│   │   ├── accessors_indexes_test.go
│   │   ├── accessors_metadata.go
│   │   ├── interfaces.go
│   │   └── schema.go
│   ├── state
│   │   ├── database.go
│   │   ├── dump.go
│   │   ├── iterator.go
│   │   ├── iterator_test.go
│   │   ├── journal.go
│   │   ├── main_test.go
│   │   ├── managed_state.go
│   │   ├── managed_state_test.go
│   │   ├── statedb.go
│   │   ├── statedb_test.go
│   │   ├── state_object.go
│   │   ├── state_test.go
│   │   ├── sync.go
│   │   └── sync_test.go
│   ├── state_processor.go
│   ├── state_transition.go
│   ├── tx_cacher.go
│   ├── tx_journal.go
│   ├── tx_list.go
│   ├── tx_list_test.go
│   ├── tx_pool.go
│   ├── tx_pool_test.go
│   ├── types
│   │   ├── block.go
│   │   ├── block_test.go
│   │   ├── bloom9.go
│   │   ├── bloom9_test.go
│   │   ├── derive_sha.go
│   │   ├── gen_header_json.go
│   │   ├── gen_log_json.go
│   │   ├── gen_receipt_json.go
│   │   ├── gen_tx_json.go
│   │   ├── log.go
│   │   ├── log_test.go
│   │   ├── receipt.go
│   │   ├── transaction.go
│   │   ├── transaction_signing.go
│   │   ├── transaction_signing_test.go
│   │   └── transaction_test.go
│   ├── types.go
│   └── vm
│       ├── analysis.go
│       ├── analysis_test.go
│       ├── common.go
│       ├── contract.go
│       ├── contracts.go
│       ├── contracts_test.go
│       ├── doc.go
│       ├── errors.go
│       ├── evm.go
│       ├── gas.go
│       ├── gas_table.go
│       ├── gas_table_test.go
│       ├── gen_structlog.go
│       ├── instructions.go
│       ├── instructions_test.go
│       ├── interface.go
│       ├── interpreter.go
│       ├── intpool.go
│       ├── intpool_test.go
│       ├── int_pool_verifier_empty.go
│       ├── int_pool_verifier.go
│       ├── jump_table.go
│       ├── logger.go
│       ├── logger_test.go
│       ├── memory.go
│       ├── memory_table.go
│       ├── noop.go
│       ├── opcodes.go
│       ├── runtime
│       │   ├── doc.go
│       │   ├── env.go
│       │   ├── fuzz.go
│       │   ├── runtime_example_test.go
│       │   ├── runtime.go
│       │   └── runtime_test.go
│       ├── stack.go
│       └── stack_table.go
├── crypto
│   ├── bn256
│   │   ├── bn256_fast.go
│   │   ├── bn256_fuzz.go
│   │   ├── bn256_slow.go
│   │   ├── cloudflare
│   │   │   ├── bn256.go
│   │   │   ├── bn256_test.go
│   │   │   ├── constants.go
│   │   │   ├── curve.go
│   │   │   ├── example_test.go
│   │   │   ├── gfp12.go
│   │   │   ├── gfp2.go
│   │   │   ├── gfp6.go
│   │   │   ├── gfp_decl.go
│   │   │   ├── gfp_generic.go
│   │   │   ├── gfp.go
│   │   │   ├── gfp_test.go
│   │   │   ├── lattice.go
│   │   │   ├── lattice_test.go
│   │   │   ├── main_test.go
│   │   │   ├── optate.go
│   │   │   └── twist.go
│   │   └── google
│   │       ├── bn256.go
│   │       ├── bn256_test.go
│   │       ├── constants.go
│   │       ├── curve.go
│   │       ├── example_test.go
│   │       ├── gfp12.go
│   │       ├── gfp2.go
│   │       ├── gfp6.go
│   │       ├── main_test.go
│   │       ├── optate.go
│   │       └── twist.go
│   ├── crypto.go
│   ├── crypto_test.go
│   ├── ecies
│   │   ├── ecies.go
│   │   ├── ecies_test.go
│   │   └── params.go
│   ├── secp256k1
│   │   ├── curve.go
│   │   ├── libsecp256k1
│   │   │   ├── build-aux
│   │   │   │   └── m4
│   │   │   ├── contrib
│   │   │   ├── include
│   │   │   ├── obj
│   │   │   ├── sage
│   │   │   └── src
│   │   │       ├── asm
│   │   │       ├── java
│   │   │       │   └── org
│   │   │       │       └── bitcoin
│   │   │       └── modules
│   │   │           ├── ecdh
│   │   │           └── recovery
│   │   ├── panic_cb.go
│   │   ├── secp256.go
│   │   └── secp256_test.go
│   ├── sha3
│   │   ├── doc.go
│   │   ├── hashes.go
│   │   ├── keccakf_amd64.go
│   │   ├── keccakf.go
│   │   ├── register.go
│   │   ├── sha3.go
│   │   ├── sha3_test.go
│   │   ├── shake.go
│   │   ├── testdata
│   │   ├── xor_generic.go
│   │   ├── xor.go
│   │   └── xor_unaligned.go
│   ├── signature_cgo.go
│   ├── signature_nocgo.go
│   └── signature_test.go
├── dashboard
│   ├── assets
│   │   ├── components
│   │   └── types
│   ├── assets.go
│   ├── config.go
│   ├── cpu.go
│   ├── cpu_windows.go
│   ├── dashboard.go
│   ├── log.go
│   └── message.go
├── eth
│   ├── api_backend.go
│   ├── api.go
│   ├── api_test.go
│   ├── api_tracer.go
│   ├── backend.go
│   ├── bloombits.go
│   ├── config.go
│   ├── downloader
│   │   ├── api.go
│   │   ├── downloader.go
│   │   ├── downloader_test.go
│   │   ├── events.go
│   │   ├── fakepeer.go
│   │   ├── metrics.go
│   │   ├── modes.go
│   │   ├── peer.go
│   │   ├── queue.go
│   │   ├── statesync.go
│   │   └── types.go
│   ├── fetcher
│   │   ├── fetcher.go
│   │   ├── fetcher_test.go
│   │   └── metrics.go
│   ├── filters
│   │   ├── api.go
│   │   ├── api_test.go
│   │   ├── bench_test.go
│   │   ├── filter.go
│   │   ├── filter_system.go
│   │   ├── filter_system_test.go
│   │   └── filter_test.go
│   ├── gasprice
│   │   └── gasprice.go
│   ├── gen_config.go
│   ├── handler.go
│   ├── handler_test.go
│   ├── helper_test.go
│   ├── metrics.go
│   ├── peer.go
│   ├── protocol.go
│   ├── protocol_test.go
│   ├── sync.go
│   ├── sync_test.go
│   └── tracers
│       ├── internal
│       │   └── tracers
│       │       ├── assets.go
│       │       └── tracers.go
│       ├── testdata
│       ├── tracer.go
│       ├── tracers.go
│       ├── tracers_test.go
│       └── tracer_test.go
├── ethclient
│   ├── ethclient.go
│   ├── ethclient_test.go
│   └── signer.go
├── ethdb
│   ├── database.go
│   ├── database_test.go
│   ├── interface.go
│   └── memory_database.go
├── ethstats
│   └── ethstats.go
├── event
│   ├── event.go
│   ├── event_test.go
│   ├── example_feed_test.go
│   ├── example_scope_test.go
│   ├── example_subscription_test.go
│   ├── example_test.go
│   ├── feed.go
│   ├── feed_test.go
│   ├── filter
│   │   ├── filter.go
│   │   ├── filter_test.go
│   │   └── generic_filter.go
│   ├── subscription.go
│   └── subscription_test.go
├── interfaces.go
├── internal
│   ├── build
│   │   ├── archive.go
│   │   ├── azure.go
│   │   ├── env.go
│   │   ├── pgp.go
│   │   └── util.go
│   ├── cmdtest
│   │   └── test_cmd.go
│   ├── debug
│   │   ├── api.go
│   │   ├── flags.go
│   │   ├── loudpanic_fallback.go
│   │   ├── loudpanic.go
│   │   ├── trace_fallback.go
│   │   └── trace.go
│   ├── ethapi
│   │   ├── addrlock.go
│   │   ├── api.go
│   │   └── backend.go
│   ├── guide
│   │   ├── guide.go
│   │   └── guide_test.go
│   ├── jsre
│   │   ├── completion.go
│   │   ├── completion_test.go
│   │   ├── deps
│   │   │   ├── bindata.go
│   │   │   └── deps.go
│   │   ├── jsre.go
│   │   ├── jsre_test.go
│   │   └── pretty.go
│   └── web3ext
│       └── web3ext.go
├── les
│   ├── api_backend.go
│   ├── backend.go
│   ├── bloombits.go
│   ├── distributor.go
│   ├── distributor_test.go
│   ├── execqueue.go
│   ├── execqueue_test.go
│   ├── fetcher.go
│   ├── flowcontrol
│   │   ├── control.go
│   │   └── manager.go
│   ├── handler.go
│   ├── handler_test.go
│   ├── helper_test.go
│   ├── metrics.go
│   ├── odr.go
│   ├── odr_requests.go
│   ├── odr_test.go
│   ├── peer.go
│   ├── protocol.go
│   ├── randselect.go
│   ├── randselect_test.go
│   ├── request_test.go
│   ├── retrieve.go
│   ├── server.go
│   ├── serverpool.go
│   ├── sync.go
│   └── txrelay.go
├── light
│   ├── lightchain.go
│   ├── lightchain_test.go
│   ├── nodeset.go
│   ├── odr.go
│   ├── odr_test.go
│   ├── odr_util.go
│   ├── postprocess.go
│   ├── trie.go
│   ├── trie_test.go
│   ├── txpool.go
│   └── txpool_test.go
├── log
│   ├── doc.go
│   ├── format.go
│   ├── handler_glog.go
│   ├── handler.go
│   ├── handler_go13.go
│   ├── handler_go14.go
│   ├── logger.go
│   ├── root.go
│   ├── syslog.go
│   └── term
│       ├── terminal_appengine.go
│       ├── terminal_darwin.go
│       ├── terminal_freebsd.go
│       ├── terminal_linux.go
│       ├── terminal_netbsd.go
│       ├── terminal_notwindows.go
│       ├── terminal_openbsd.go
│       ├── terminal_solaris.go
│       └── terminal_windows.go
├── metrics
│   ├── counter.go
│   ├── counter_test.go
│   ├── debug.go
│   ├── debug_test.go
│   ├── disk.go
│   ├── disk_linux.go
│   ├── disk_nop.go
│   ├── ewma.go
│   ├── ewma_test.go
│   ├── exp
│   │   └── exp.go
│   ├── gauge_float64.go
│   ├── gauge_float64_test.go
│   ├── gauge.go
│   ├── gauge_test.go
│   ├── graphite.go
│   ├── graphite_test.go
│   ├── healthcheck.go
│   ├── histogram.go
│   ├── histogram_test.go
│   ├── influxdb
│   │   └── influxdb.go
│   ├── init_test.go
│   ├── json.go
│   ├── json_test.go
│   ├── librato
│   │   ├── client.go
│   │   └── librato.go
│   ├── log.go
│   ├── meter.go
│   ├── meter_test.go
│   ├── metrics.go
│   ├── metrics_test.go
│   ├── opentsdb.go
│   ├── opentsdb_test.go
│   ├── registry.go
│   ├── registry_test.go
│   ├── resetting_timer.go
│   ├── resetting_timer_test.go
│   ├── runtime_cgo.go
│   ├── runtime_gccpufraction.go
│   ├── runtime.go
│   ├── runtime_no_cgo.go
│   ├── runtime_no_gccpufraction.go
│   ├── runtime_test.go
│   ├── sample.go
│   ├── sample_test.go
│   ├── syslog.go
│   ├── timer.go
│   ├── timer_test.go
│   ├── writer.go
│   └── writer_test.go
├── miner
│   ├── agent.go
│   ├── miner.go
│   ├── unconfirmed.go
│   ├── unconfirmed_test.go
│   └── worker.go
├── mobile
│   ├── accounts.go
│   ├── android_test.go
│   ├── big.go
│   ├── bind.go
│   ├── common.go
│   ├── context.go
│   ├── discover.go
│   ├── doc.go
│   ├── ethclient.go
│   ├── ethereum.go
│   ├── geth_android.go
│   ├── geth.go
│   ├── geth_ios.go
│   ├── geth_other.go
│   ├── init.go
│   ├── interface.go
│   ├── logger.go
│   ├── p2p.go
│   ├── params.go
│   ├── primitives.go
│   ├── types.go
│   └── vm.go
├── node
│   ├── api.go
│   ├── config.go
│   ├── config_test.go
│   ├── defaults.go
│   ├── doc.go
│   ├── errors.go
│   ├── node_example_test.go
│   ├── node.go
│   ├── node_test.go
│   ├── service.go
│   ├── service_test.go
│   └── utils_test.go
├── p2p
│   ├── dial.go
│   ├── dial_test.go
│   ├── discover
│   │   ├── database.go
│   │   ├── database_test.go
│   │   ├── node.go
│   │   ├── node_test.go
│   │   ├── ntp.go
│   │   ├── table.go
│   │   ├── table_test.go
│   │   ├── udp.go
│   │   └── udp_test.go
│   ├── discv5
│   │   ├── database.go
│   │   ├── database_test.go
│   │   ├── metrics.go
│   │   ├── net.go
│   │   ├── net_test.go
│   │   ├── nodeevent_string.go
│   │   ├── node.go
│   │   ├── node_test.go
│   │   ├── ntp.go
│   │   ├── sim_run_test.go
│   │   ├── sim_test.go
│   │   ├── sim_testmain_test.go
│   │   ├── table.go
│   │   ├── table_test.go
│   │   ├── ticket.go
│   │   ├── topic.go
│   │   ├── topic_test.go
│   │   ├── udp.go
│   │   └── udp_test.go
│   ├── enr
│   │   ├── enr.go
│   │   ├── enr_test.go
│   │   ├── entries.go
│   │   ├── idscheme.go
│   │   └── idscheme_test.go
│   ├── message.go
│   ├── message_test.go
│   ├── metrics.go
│   ├── nat
│   │   ├── nat.go
│   │   ├── natpmp.go
│   │   ├── nat_test.go
│   │   ├── natupnp.go
│   │   └── natupnp_test.go
│   ├── netutil
│   │   ├── error.go
│   │   ├── error_test.go
│   │   ├── net.go
│   │   ├── net_test.go
│   │   ├── toobig_notwindows.go
│   │   └── toobig_windows.go
│   ├── peer_error.go
│   ├── peer.go
│   ├── peer_test.go
│   ├── protocol.go
│   ├── protocols
│   │   ├── protocol.go
│   │   └── protocol_test.go
│   ├── rlpx.go
│   ├── rlpx_test.go
│   ├── server.go
│   ├── server_test.go
│   ├── simulations
│   │   ├── adapters
│   │   │   ├── docker.go
│   │   │   ├── exec.go
│   │   │   ├── inproc.go
│   │   │   ├── inproc_test.go
│   │   │   ├── types.go
│   │   │   ├── ws.go
│   │   │   └── ws_test.go
│   │   ├── events.go
│   │   ├── examples
│   │   │   └── ping-pong.go
│   │   ├── http.go
│   │   ├── http_test.go
│   │   ├── mocker.go
│   │   ├── mocker_test.go
│   │   ├── network.go
│   │   ├── network_test.go
│   │   ├── pipes
│   │   │   └── pipes.go
│   │   └── simulation.go
│   └── testing
│       ├── peerpool.go
│       ├── protocolsession.go
│       └── protocoltester.go
├── params
│   ├── bootnodes.go
│   ├── config.go
│   ├── config_test.go
│   ├── dao.go
│   ├── denomination.go
│   ├── gas_table.go
│   ├── network_params.go
│   ├── protocol_params.go
│   └── version.go
├── rlp
│   ├── decode.go
│   ├── decode_tail_test.go
│   ├── decode_test.go
│   ├── doc.go
│   ├── encode.go
│   ├── encoder_example_test.go
│   ├── encode_test.go
│   ├── raw.go
│   ├── raw_test.go
│   └── typecache.go
├── rpc
│   ├── client_example_test.go
│   ├── client.go
│   ├── client_test.go
│   ├── doc.go
│   ├── endpoints.go
│   ├── errors.go
│   ├── http.go
│   ├── http_test.go
│   ├── inproc.go
│   ├── ipc.go
│   ├── ipc_unix.go
│   ├── ipc_windows.go
│   ├── json.go
│   ├── json_test.go
│   ├── server.go
│   ├── server_test.go
│   ├── subscription.go
│   ├── subscription_test.go
│   ├── types.go
│   ├── types_test.go
│   ├── utils.go
│   ├── utils_test.go
│   └── websocket.go
├── signer
│   ├── core
│   │   ├── abihelper.go
│   │   ├── abihelper_test.go
│   │   ├── api.go
│   │   ├── api_test.go
│   │   ├── auditlog.go
│   │   ├── cliui.go
│   │   ├── stdioui.go
│   │   ├── types.go
│   │   ├── validation.go
│   │   └── validation_test.go
│   ├── rules
│   │   ├── deps
│   │   │   ├── bindata.go
│   │   │   └── deps.go
│   │   ├── rules.go
│   │   └── rules_test.go
│   └── storage
│       ├── aes_gcm_storage.go
│       ├── aes_gcm_storage_test.go
│       └── storage.go
├── swarm
│   ├── api
│   │   ├── api.go
│   │   ├── api_test.go
│   │   ├── client
│   │   │   ├── client.go
│   │   │   └── client_test.go
│   │   ├── config.go
│   │   ├── config_test.go
│   │   ├── filesystem.go
│   │   ├── filesystem_test.go
│   │   ├── http
│   │   │   ├── middleware.go
│   │   │   ├── response.go
│   │   │   ├── response_test.go
│   │   │   ├── roundtripper.go
│   │   │   ├── roundtripper_test.go
│   │   │   ├── sctx.go
│   │   │   ├── server.go
│   │   │   ├── server_test.go
│   │   │   └── templates.go
│   │   ├── manifest.go
│   │   ├── manifest_test.go
│   │   ├── storage.go
│   │   ├── storage_test.go
│   │   ├── testapi.go
│   │   ├── testdata
│   │   │   └── test0
│   │   │       └── img
│   │   ├── uri.go
│   │   └── uri_test.go
│   ├── bmt
│   │   ├── bmt.go
│   │   ├── bmt_r.go
│   │   └── bmt_test.go
│   ├── dev
│   │   └── scripts
│   ├── fuse
│   │   ├── fuse_dir.go
│   │   ├── fuse_file.go
│   │   ├── fuse_root.go
│   │   ├── swarmfs_fallback.go
│   │   ├── swarmfs.go
│   │   ├── swarmfs_test.go
│   │   ├── swarmfs_unix.go
│   │   └── swarmfs_util.go
│   ├── grafana_dashboards
│   ├── log
│   │   └── log.go
│   ├── metrics
│   │   └── flags.go
│   ├── multihash
│   │   ├── multihash.go
│   │   └── multihash_test.go
│   ├── network
│   │   ├── bitvector
│   │   │   ├── bitvector.go
│   │   │   └── bitvector_test.go
│   │   ├── common.go
│   │   ├── discovery.go
│   │   ├── discovery_test.go
│   │   ├── hive.go
│   │   ├── hive_test.go
│   │   ├── kademlia.go
│   │   ├── kademlia_test.go
│   │   ├── networkid_test.go
│   │   ├── priorityqueue
│   │   │   ├── priorityqueue.go
│   │   │   └── priorityqueue_test.go
│   │   ├── protocol.go
│   │   ├── protocol_test.go
│   │   ├── simulation
│   │   │   ├── bucket.go
│   │   │   ├── bucket_test.go
│   │   │   ├── connect.go
│   │   │   ├── connect_test.go
│   │   │   ├── events.go
│   │   │   ├── events_test.go
│   │   │   ├── example_test.go
│   │   │   ├── http.go
│   │   │   ├── http_test.go
│   │   │   ├── kademlia.go
│   │   │   ├── kademlia_test.go
│   │   │   ├── node.go
│   │   │   ├── node_test.go
│   │   │   ├── service.go
│   │   │   ├── service_test.go
│   │   │   ├── simulation.go
│   │   │   └── simulation_test.go
│   │   ├── simulations
│   │   │   ├── discovery
│   │   │   │   ├── discovery.go
│   │   │   │   └── discovery_test.go
│   │   │   ├── overlay.go
│   │   │   └── overlay_test.go
│   │   └── stream
│   │       ├── common_test.go
│   │       ├── delivery.go
│   │       ├── delivery_test.go
│   │       ├── intervals
│   │       │   ├── dbstore_test.go
│   │       │   ├── intervals.go
│   │       │   ├── intervals_test.go
│   │       │   └── store_test.go
│   │       ├── intervals_test.go
│   │       ├── messages.go
│   │       ├── peer.go
│   │       ├── snapshot_retrieval_test.go
│   │       ├── snapshot_sync_test.go
│   │       ├── streamer_test.go
│   │       ├── stream.go
│   │       ├── syncer.go
│   │       ├── syncer_test.go
│   │       └── testing
│   ├── network_test.go
│   ├── pot
│   │   ├── address.go
│   │   ├── doc.go
│   │   ├── pot.go
│   │   └── pot_test.go
│   ├── pss
│   │   ├── api.go
│   │   ├── client
│   │   │   ├── client.go
│   │   │   ├── client_test.go
│   │   │   └── doc.go
│   │   ├── doc.go
│   │   ├── handshake.go
│   │   ├── handshake_none.go
│   │   ├── handshake_test.go
│   │   ├── notify
│   │   │   ├── notify.go
│   │   │   └── notify_test.go
│   │   ├── ping.go
│   │   ├── protocol.go
│   │   ├── protocol_none.go
│   │   ├── protocol_test.go
│   │   ├── pss.go
│   │   ├── pss_test.go
│   │   ├── testdata
│   │   └── types.go
│   ├── sctx
│   │   └── sctx.go
│   ├── services
│   │   └── swap
│   │       ├── swap
│   │       │   ├── swap.go
│   │       │   └── swap_test.go
│   │       └── swap.go
│   ├── spancontext
│   │   └── spancontext.go
│   ├── state
│   │   ├── dbstore.go
│   │   ├── dbstore_test.go
│   │   ├── inmemorystore.go
│   │   └── store.go
│   ├── state.go
│   ├── storage
│   │   ├── chunker.go
│   │   ├── chunker_test.go
│   │   ├── chunkstore.go
│   │   ├── common.go
│   │   ├── common_test.go
│   │   ├── database.go
│   │   ├── dbapi.go
│   │   ├── encryption
│   │   │   ├── encryption.go
│   │   │   └── encryption_test.go
│   │   ├── error.go
│   │   ├── filestore.go
│   │   ├── filestore_test.go
│   │   ├── hasherstore.go
│   │   ├── hasherstore_test.go
│   │   ├── ldbstore.go
│   │   ├── ldbstore_test.go
│   │   ├── localstore.go
│   │   ├── localstore_test.go
│   │   ├── memstore.go
│   │   ├── memstore_test.go
│   │   ├── mock
│   │   │   ├── db
│   │   │   │   ├── db.go
│   │   │   │   └── db_test.go
│   │   │   ├── mem
│   │   │   │   ├── mem.go
│   │   │   │   └── mem_test.go
│   │   │   ├── mock.go
│   │   │   ├── rpc
│   │   │   │   ├── rpc.go
│   │   │   │   └── rpc_test.go
│   │   │   └── test
│   │   │       └── test.go
│   │   ├── mru
│   │   │   ├── doc.go
│   │   │   ├── error.go
│   │   │   ├── handler.go
│   │   │   ├── lookup.go
│   │   │   ├── lookup_test.go
│   │   │   ├── metadata.go
│   │   │   ├── metadata_test.go
│   │   │   ├── request.go
│   │   │   ├── request_test.go
│   │   │   ├── resource.go
│   │   │   ├── resource_sign.go
│   │   │   ├── resource_test.go
│   │   │   ├── signedupdate.go
│   │   │   ├── testutil.go
│   │   │   ├── timestampprovider.go
│   │   │   ├── update.go
│   │   │   ├── updateheader.go
│   │   │   ├── updateheader_test.go
│   │   │   └── update_test.go
│   │   ├── netstore.go
│   │   ├── netstore_test.go
│   │   ├── pyramid.go
│   │   ├── swarmhasher.go
│   │   └── types.go
│   ├── swarm.go
│   ├── swarm_test.go
│   ├── testutil
│   │   └── http.go
│   ├── tracing
│   │   └── tracing.go
│   └── version
│       └── version.go
├── trie
│   ├── database.go
│   ├── encoding.go
│   ├── encoding_test.go
│   ├── errors.go
│   ├── hasher.go
│   ├── iterator.go
│   ├── iterator_test.go
│   ├── node.go
│   ├── node_test.go
│   ├── proof.go
│   ├── proof_test.go
│   ├── secure_trie.go
│   ├── secure_trie_test.go
│   ├── sync.go
│   ├── sync_test.go
│   ├── trie.go
│   └── trie_test.go
└── whisper
    ├── mailserver
    │   ├── mailserver.go
    │   └── server_test.go
    ├── shhclient
    │   └── client.go
    ├── whisperv5
    │   ├── api.go
    │   ├── benchmarks_test.go
    │   ├── config.go
    │   ├── doc.go
    │   ├── envelope.go
    │   ├── filter.go
    │   ├── filter_test.go
    │   ├── gen_criteria_json.go
    │   ├── gen_message_json.go
    │   ├── gen_newmessage_json.go
    │   ├── message.go
    │   ├── message_test.go
    │   ├── peer.go
    │   ├── peer_test.go
    │   ├── topic.go
    │   ├── topic_test.go
    │   ├── whisper.go
    │   └── whisper_test.go
    └── whisperv6
        ├── api.go
        ├── api_test.go
        ├── benchmarks_test.go
        ├── config.go
        ├── doc.go
        ├── envelope.go
        ├── envelope_test.go
        ├── filter.go
        ├── filter_test.go
        ├── gen_criteria_json.go
        ├── gen_message_json.go
        ├── gen_newmessage_json.go
        ├── message.go
        ├── message_test.go
        ├── peer.go
        ├── peer_test.go
        ├── topic.go
        ├── topic_test.go
        ├── whisper.go
        └── whisper_test.go


```