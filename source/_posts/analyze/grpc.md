---
title: grpc
date: 2018-05-22 15:08:18
categories: [项目分析]
---

<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 一个简易的example底层都做了哪些事?](#2-一个简易的example底层都做了哪些事)

<!-- /TOC -->


<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源

* https://grpc.io/
* https://grpc.io/docs/quickstart/go.html (go quick start)



<a id="markdown-2-一个简易的example底层都做了哪些事" name="2-一个简易的example底层都做了哪些事"></a>
# 2. 一个简易的example底层都做了哪些事?

```bash
# server

type server struct{}
func (s *server) Solve(ctx context.Context, in *pb.SolveRequest) (*pb.SolveReply, error) {}

s := grpc.NewServer()

pb.RegisterSudokuSolverServer(s, &server{})

reflection.Register(s)

s.Serve(listener)

```

```bash
# client

conn, err := grpc.Dial(arg[1], grpc.WithInsecure())

c := pb.NewSudokuSolverClient(conn)

ctx, cancel := context.WithTimeout(context.Background(), time.Second)

r, err := c.Solve(ctx, &pb.SolveRequest{Problem: arg[2]})

```
