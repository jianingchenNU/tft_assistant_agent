# TFT Assistant Agent

一个轻量的 Python agent 项目骨架，暂时不绑定具体模型供应商。

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

运行本地占位模型：

```bash
tft-agent "推荐一个适合新手的阵容"
```

当前命令行使用 `EchoModel` 作为占位实现。接入真实模型时，只需要实现
`Model.complete()`，再在 `cli.py` 中替换模型即可。

## 配置

复制 `.env.example` 作为配置参考。当前配置通过环境变量读取：

- `TFT_AGENT_MODEL`
- `TFT_AGENT_LOG_LEVEL`
- `TFT_AGENT_MAX_STEPS`
- `TFT_AGENT_SYSTEM_PROMPT`

## 测试

```bash
python -m unittest discover -s tests -v
```
