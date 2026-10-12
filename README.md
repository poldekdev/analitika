# analitika

> Analitika is a chart generator written in Python, which uses a JSON-based configuration

## How to use

```bash
python main.py <your config.json path> -o [output file path]
```

## Basics of configuration
> Configuration is based on [Pydantic models](https://pydantic.dev/docs/validation/dev/get-started/)
> 
> Which are located [here](src/analitika/config/)
>
> Example `config.json` file looks something like this (for "bar" type):
```json
{
  "type": "bar",
  "module_config": {
    "categories": [
      "A",
      "B",
      "C"
    ],
    "values": [
      1,
      2,
      3
    ],
    "title": "Test"
  }
}
```
