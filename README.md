# Portifolio Projects to Learn Programming and Data Science

These will be my forays into learning techniques for data science. I'll track my
projects here with a quick note on what each project does.

## Natural Language Processing - NLP

In this code I used NLP techniques to interpret text data that I was working with in my PhD and to learn some techniques I was going to use in other context. The text used to perform this analysis was a transcript of a chemistry class for undergraduation students.

I've started with pre-processing techniques including tokenization, text normalization and data cleaning. Once in a standard format, various regular and machine learning techniques can be applied to better understand the data. First I did a classic word cloud to visualize the text.

![Word Cloud](nlp-learning/output/images/wordcloud.png)


Also worked with modeling techniques to score the sentiment of a text. To perform a sentiment analysis, I did a subjectivity score to understand how much the teacher speech was opiniated (if what he was saying was a objective fact or a subjective opinion) and a polarity score to understand if what he is talking is negative or positive.

![Sentiment Analysis](nlp-learning/output/images/sentiment2.png)

## Educação ES

In this code I analysed educational data from my home state using data from Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). The institute is responsible for promoting studies, research and periodic evaluations on the Brazilian educational system, with the objective of subsidizing the formulation and implementation of public policies for the educational area.

This is an analisys of elementary schools per cities aggregating them by their administrative instance (municipal, state, federal or private).

**Elementary**
![Schools per City - Instance](output/images/type_school_city_fundamental.png)

**Middle School**
![Schools per City - Instance](output/images/type_school_city_medio.png)
