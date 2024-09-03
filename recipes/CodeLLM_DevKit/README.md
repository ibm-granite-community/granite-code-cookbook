# CodeLLM-Devkit: A Python library for seamless interaction with CodeLLMs

Codellm-devkit (CLDK) is a multilingual program analysis framework that bridges the gap between traditional static analysis tools and Large Language Models (LLMs) specialized for code (CodeLLMs). Codellm-devkit allows developers to streamline the process of transforming raw code into actionable insights by providing a unified interface for integrating outputs from various analysis tools and preparing them for effective use by CodeLLMs.

Codellm-devkit simplifies the complex process of analyzing codebases that span multiple programming languages, making it easier to extract meaningful insights and drive LLM-based code analysis. `CLDK` achieves this through an open-source Python library that abstracts the intricacies of program analysis and LLM interactions. With this library, the developer can streamline the process of transforming raw code into actionable insights by providing a unified interface for integrating outputs from various analysis tools and preparing them for effective use by CodeLLMs.

For more details, please refer to CLDK GitHub [repository](https://github.com/IBM/codellm-devkit/tree/main).

There are example recipes:

* [Code Sumarization](./code_summarization.ipynb) - Summarize what a Java method does.
* [Generate Unit Tests](./generate_unit_tests.ipynb) - Generate unit tests for Java code.
* [Validating Code](./validating_code.ipynb) - Translate Java code to Python and analyze it for correctness.

Please start with the [Code Sumarization](./code_summarization.ipynb) tutorial, as it provides set up instructions that won't be repeated in the other notebooks.

The recipes download Java example code to a temporary directory `./temp`. When you are finished with these recipes, you can safely delete this directory, e.g.,

```shell
rm -rf temp
```
