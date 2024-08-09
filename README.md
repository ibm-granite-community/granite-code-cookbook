# Granite Code Cookbook

The "Recipes" in the Granite Code Cookbook showcase the capabilites of
the Granite Code models.

## Contents

The Granite Code Cookbook is still in early development.

## Contributing

### General Requirements

For information about contributing to this repo, code of conduct guidelines, etc., see the [community](https://github.com/granite-cookbooks/community) project.  All commits are required to be DCO-signed.  The GitHub Recommended code security settings are enforced on this public repository.

### What is a "Recipe"?

A "cookbook" is composed of "recipes".
In this version of the Granite Code Cookbook, a "recipe" is a Python notebook.

Under the implied cooking analogy, there are three key defining elements of a
good recipe:

1. It clearly states the required ingredients and tools up front
2. It is straightforward to reproduce efficiently
3. It results in something delicious to eat

The "ingredients" and "tools" of the first point mean the data and software at hand.

The second point is straightford to map into the technical space:
The reader should be able to run the cells of the notebook sequentially
and the same result as what was published in the original notebook.
Our objective is to make these recipes reproducible in 15 minutes or less.
This may inform the decisions about recipe granularity.

The third point is more subtle, and is what sets this kind of writing apart.
In a technical sense, "something delicious to eat" means a system
that demonstrates useful functionality in such a way that it sets the
reader on the path to adopting it in their environment.  It clearly articulate the busines value achieved by the resulting system.

For a "text to sql" recipe, for instance, the recipe should:

- State at a high level how a "text to sql" capability could create "business value", and therefore be worth the investment.
- Provide example schema
- Provide example data
- Provide example natural language queries
- Show the expected resulting SQL
- Provide enough code to walk through the whole process
- Remind or show the reader how to obtain the schema and execute the query.

For recipe authors with strong familiarity with a specific capability or tool,
the first inclination may be to write a recipe oriented around the tool.
Consider alternate ways to phrase the recipe so that the end result is showcased, rather than the tool.

Under the cooking analogy, that would mean writing a great soup recipe rather than one that talks about the features of a food processor.  If the soup tastes great and is easy to prepare, the reader will likely want to know more about how it was made.

Recipes will vary in complexity.
Some may be single inference calls.
Others may illustrate useful agentic workflows.

A "cookbook" is not intended to be a comprehensive guide to all
issues that may arise during development with Granite Code.
Recipes will link to helpful external resources on topics including: distributed systems, UI, design, AI/ML theory, metrics, etc.

### Exceptions

While the majority of the content in the Granite Code Cookbook
should be "recipes", there will be a need for other kinds of exposition.

Relating to Granite Code, these might include:

- Generally useful VS Code plugins
- Application frameworks such as LangChain (and LangServe, LangGgraph, ...) and LlamaIndex

### Granite Code

The common element of all the recipes in this Cookbook is either direct usage of a Granite Code model, or strong relevance to those models.

### Everything Local (... except, perhaps, the model)

Minimize the reader's exposure to sign-up flows and stateful network calls.

In most cases, the user should expect to do a single `git clone`,
run a notebook, and then optionally do some `pip install` early in
the execution of the notebook.

The recipes should not depend on the model being either remotely hosted
or local.  It is OK for a recipe to make a choice, but providing a link
to instructions for the other choice is useful.

### Automated Validation

The code in the recipes will be automatically validated (coming soon).
Minimally, this should guarantee that no unexpected errors occur.
Checking deeper assertions about the behavior of the code
in the cells is preferred.

### Performance

Where available and appropriate, cite specific relevant expectations
and claims for quality, latency, cost, or any other relevant metrics.

In some cases, it may be appropriate to include a demonstration
of establishing those benchmarks.

### Other general guidance

- The Developer Certificate of Origin (DCO) applies to the code, documentation, and any example data provided. See [community](https://github.com/granite-cookbooks/community) for more on the DCO.
- Prefer an opinionated recipe over one that is flexible
- With that said, sometimes offering examples from multiple domains (eg for "text to sql") can be helpful.  If that brings too much complexity, split into smaller recipes.
- Keep in mind a specific user persona when writing a recipe.  Rather than writing for a general audience, can you imagine that one specific user would find the recipe valueable from beginning to end?
- Take an iterative approach to the development of this Cookbook.
- Expect that over time, recipes will be split, merged, made uniform, deprecated, replace, or deleted.
- The `granite-cookbooks` org is not the place to host OSS "code" other than what is directy visible in the recipes and simple utility functions.
