## Web Service LLM:

An API that extracts meaningful attributes from a HTML block of an e-commerce website using an open source large langauge model and returns the relevant and meaningful information from the page in JSON format.

The steps are as follows, to complete this task.

1. First we create a block diagram of how the input, processing and ouptut flow.

![LLM Block diagram](LLM.png)

2.Create a virtual environment, since I have mini conda, I wil create virtual env with the help of miniconda
- conda create --name llm_api
- conda activate myenv
to deactivate the virtual env:
-  conda deactivate 

Now we can install all the needed files and packages.

For the LLM, I have initially chosen the open source Llama 3. It can be easily installed by downloading <a href="https://ollama.com/">Ollama</a>.

![LLM Block diagram](Ollama.png)

![LLM Block diagram](Llama3.png)

Meta Llama 3, a family of models developed by Meta Inc. are new state-of-the-art , available in both 8B and 70B parameter sizes (pre-trained or instruction-tuned).