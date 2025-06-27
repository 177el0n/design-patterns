# Builder Pattern

オブジェクトの生成過程と、実際の振る舞いを分離できる。(関心の分離・単一責任の原則)  
オブジェクトの生成自体を知らなくとも必要な引数を渡すことで、  
異なるオブジェクトを複数作成することが可能。

## 各ファイルの役割
- main: workflowの実装  
- director: 特徴となる引数を渡し、特定のAgentを組み立てる  
- agent: Agent構築後の実際の振る舞いを定義  
- abstract_agent: Agentの組み立ての抽象クラス  
- agent_builder: Agent組み立ての具象クラス
