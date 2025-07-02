# Producer Consumer Pattern

タスクの生産と、タスクの消費を別のスレッドでそれぞれ行う。  
タスクの管理はQueueで行うため、それぞれのメソッドが疎結合で実行できる。  

## 各ファイルの役割
- main: Producer Consumer Patternを実行
- producer: タスクの生成と、Queueへの登録
- consumer: Queueからタスクを取得し、消費する
