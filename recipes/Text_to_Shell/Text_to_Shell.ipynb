{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "# Generating Bash Code with Granite Code and Ollama\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **NOTE:** This recipe assumes you are working on a Linux, MacOS, or other UNIX-compatible system. While we haven't tested on Windows, some of the examples may generate valid DOS or PowerShell output. See comments below.\n",
    "\n",
    "### Prerequisite: Install Ollama and Granite Code models\n",
    "\n",
    "1. [Download and install Ollama](https://ollama.com/download), if you haven't already.\n",
    "1. Start the Ollama server: `ollama serve`\n",
    "\n",
    "Now, in a new terminal window, install one or more of the following Granite Code models. The smallest model `3b` works better on machines with limited resources, but doesn't produce very good results for this notebook. The `8b` model works better and the `20b` model works best, if you are able to use it.\n",
    "\n",
    "```shell\n",
    "ollama pull granite-code:3b\n",
    "ollama pull granite-code:8b\n",
    "ollama pull granite-code:20b\n",
    "```\n",
    "\n",
    "> **NOTE:** By default, this notebook only uses the `3b` model to ensure the widest set of users can run the code. This is also necessary for our CI/CD unit test environment. However, if you have access to a reasonably new and powerful machine, we recommend using the `8b` or the `20b` version instead.\n",
    ">\n",
    "> Change the value in the next cell if you decide to use the `8b` or `20b` model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "default_model = 'granite-code:3b'  # The `8b` and `20b` models work better!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install ollama"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## One-shot Prompt with Granite Code 3b\n",
    "\n",
    "In One-shot prompting, you provide the model with a question and no examples. The model will generate an answer given its training. Larger models tend to do better at this task.\n",
    "\n",
    "Use the [ollama-python package](https://github.com/ollama/ollama-python) to access the model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ollama"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's write two helper functions that we'll use for all our queries. First, we'll find it useful to determine the name of our operating system and use that string in queries. This is because shell commands sometimes have different options on Linux vs. MacOS, etc. We'll write our queries so they take this difference into account. Note that `platform.system()` returns `Windows` on Windows system."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **TIPS:** If you are using MacOS, you can install Linux-compatible versions of many commands. Consider these two options:\n",
    "> * Install GNU Coreutils on a Mac. See [these instructions](https://superuser.com/questions/476575/replace-os-xs-shell-commands-with-the-linux-versions).\n",
    "> * Install [HomeBrew](https://brew.sh/) and use it to install Linux-compatible (and other) tools."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import platform\n",
    "\n",
    "def os_name():\n",
    "    os_name = platform.system()\n",
    "    # It turns out, using \"MacOS\" is better than \"Darwin\", which is what gets returned on MacOS.\n",
    "    # For all other cases, the returned value should be fine as is, so we map the result to the desired\n",
    "    # name, but only for MacOS...\n",
    "    name_map = {'Darwin': 'MacOS'}\n",
    "    shell_map = {'Windows': 'DOS'} # On Windows and use Power Shell, change from `DOS` to `Power Shell`.\n",
    "    # ... then pass the os_name value as the second arg, which is used as the default return value.\n",
    "    # For the shell name, return `bash` by default. (You can change this to zsh, fish, etc.)\n",
    "    return name_map.get(os_name, os_name), shell_map.get(os_name, 'bash')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_os, my_shell = os_name()\n",
    "print(f\"My OS is {my_os}. My shell is {my_shell}.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's write a helper function for running queries, wrapping the Ollama `generate()` API call. The user specifies the prompt and a model name, which defaults to the value of `default_model` defined above. \n",
    "\n",
    "Note how we add additional context to the user's input prompt, such as _\"make sure you write code that works for _my_ system!\"_ (We'll see another way to do this below.)\n",
    "\n",
    "The reason we print the result, then return it, is to get nicely readable output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def query(prompt: str, model: str = default_model) -> str:\n",
    "\n",
    "    response = ollama.generate(  # Calling Ollama!\n",
    "        model=model,\n",
    "        prompt=f\"{prompt}. Make sure you generate {my_shell} code that is {my_os}-compatible!\")\n",
    "\n",
    "    result = response[\"response\"]\n",
    "    print(result)\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "result1 = query(f\"\"\"\n",
    "    Show me a {my_shell} script to print the first 50 files found under the current working directory\n",
    "    that have been modified within the last week. Make sure you show the last modification time\n",
    "    for each file in the output.\"\"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Remove any markdown formatting in the output and paste the commands generated into the next cell _**after the %%bash line shown**_. Also delete the `ls -l`, which is there to allow the cell to run without error if nothing is pasted there (e.g., in our CI/CD test system). So, for example, you might have something like the following:\n",
    "\n",
    "```shell\n",
    "%%bash\n",
    "find dir -type d | do_something\n",
    "...\n",
    "```\n",
    "\n",
    "The `%%bash` \"magic\" tells Jupyter to run the commands as a shell script instead of as Python code. You can omit lines like `#!/bin/bash` and keep or remove any comments `# this is a comment...`.\n",
    "\n",
    "Does the script work? If not try running the query again. Also try modifying the query string. What difference do these steps make?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "%%bash\n",
    "ls -l"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We explore execution of generated shell code in the next recipe we recommend you study after this one, [../Text_to_Shell_Exec](../Text_to_Shell_Exec/Text_to_Shell_Exec.ipynb)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Few-shot Prompting with Granite Code 3b\n",
    "\n",
    "In few-shot prompting, you provide the model with a question and some examples. The model will generate an answer given its training. The additional examples help the model zero in on a pattern, which may be required for smaller models to perform well at this task.\n",
    "\n",
    "One of the examples uses the `stat` command, which requires different syntax for Linux vs. MacOS systems.\n",
    "\n",
    "> **NOTE:** If you are using a Windows system, try changing the \"answers\" in the `examples` cell to be valid Power Shell or DOS commands. You can ignore the `stat_flags` in the next cell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stat_flags = '-c \"%y %n\" {}'\n",
    "if my_os == 'MacOS':\n",
    "    stat_flags = '-f \"%m %N\" {}'\n",
    "print(f\"The 'stat' flags for my OS \\'{my_os}\\' and shell \\'{my_shell}\\' are \\'{stat_flags}\\'\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "examples = f\"\"\"\n",
    "Question:\n",
    "Recursively find files that match '*.js', and filter out files with 'excludeddir' in their paths.\n",
    "Answer:\n",
    "find . -name '*.js' | grep -v excludeddir\n",
    "\n",
    "Question:\n",
    "Dump \\\"a0b\\\" as hexadecimal bytes\n",
    "Answer:\n",
    "printf \\\"a0b\\\" | od -tx1\n",
    "\n",
    "Question:\n",
    "create a tar ball of all pdf files in the current folder and any subdirectories.\n",
    "Answer:\n",
    "find . -name '*.pdf' | xargs tar czvf pdf.tar\n",
    "\n",
    "Question:\n",
    "Sort all files and directories in the current directory, but no subdirectories, according to modification time, and print only the seven most recently modified items\n",
    "Answer:\n",
    "find . -maxdepth 1 -exec stat {stat_flags} \\; | sort -n -r | tail -n 7\n",
    "\n",
    "Question:\n",
    "find all the empty directories in and under the current directory.\n",
    "Answer:\n",
    "find . -type d -empty\n",
    "\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's define another helper function for calling `ollama.chat()`. Why it is called `chat1()` will be explained below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def chat1(prompt: str, examples: str = examples, model: str ='granite-code:3b') -> str:\n",
    "    user_prompt = f\"\"\"\n",
    "        {examples}\n",
    "        Question:\n",
    "        {prompt}. Make sure you generate {my_shell} code that is {my_os}-compatible!\n",
    "        Answer:\"\"\"\n",
    "\n",
    "    response = ollama.chat(model=model, messages=[\n",
    "      {\n",
    "        'role': 'user',\n",
    "        'content': user_prompt\n",
    "      },\n",
    "    ])\n",
    "\n",
    "    result = response['message']['content']\n",
    "    print(result)\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "result2 = chat1(f\"\"\"\n",
    "    Show me a {my_shell} script to print the first 50 files found under the current working directory\n",
    "    that have been modified within the last week. Make sure you show the last modification time\n",
    "    for each file in the output.\"\"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Adding a System Prompt\n",
    "\n",
    "Finally, a _system prompt_ is the preferred way to provide additional instructions and clarity about the context for a task, especially when this same information applies for _all_ user queries in the application. When you are building an AI-enabled application for a set of use cases, you will probably spend a lot of time refining the system prompt to maximize the quality of the results!\n",
    "\n",
    "Here we define a `default_system_prompt` to let the model know what we expect from it.\n",
    "\n",
    "So, let's define a final helper function, `chat()`, that includes a system prompt, where `default_system_prompt` is the default. Also, note that we move the sentence `Make sure you only generate {shell} code that is {os}-compatible!` to the system prompt, where it really belongs!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "default_system_prompt = f\"\"\"\n",
    "    You are a helpful software engineer. You write clear, concise, well-commented code. \n",
    "    Make sure you only generate {my_shell} code that is {my_os}-compatible!\n",
    "    \"\"\"\n",
    "\n",
    "def chat(prompt: str,\n",
    "         system_prompt:str = default_system_prompt,\n",
    "         examples: str = examples,\n",
    "         model: str ='granite-code:3b') -> str:\n",
    "    user_prompt = f\"\"\"\n",
    "        {examples}\n",
    "        Question:\n",
    "        {prompt}\n",
    "        Answer:\"\"\"\n",
    "\n",
    "    response = ollama.chat(model=model, messages=[\n",
    "      {\n",
    "        'role':'system',\n",
    "        'content': system_prompt\n",
    "      },\n",
    "      {\n",
    "        'role': 'user',\n",
    "        'content': user_prompt\n",
    "      },\n",
    "    ])\n",
    "\n",
    "    result = response['message']['content']\n",
    "    print(result)\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "result3 = chat(f\"\"\"\n",
    "    Show me a {my_shell} script to print the first 50 files found under the current working directory\n",
    "    that have been modified within the last week. Make sure you show the last modification time\n",
    "    for each file in the output.\"\"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you modify `chat()` to return the whole `response`, what additional information do you get?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Try invoking `chat()` several times. How do the responses change from one invocation to the next? Try different queries. adding more examples to the `examples` string or modifying the ones shown. Does this affect the outputs."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
