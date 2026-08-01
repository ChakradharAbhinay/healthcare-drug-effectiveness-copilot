# Database Schema Design

## Purpose

This document describes the initial database schema for storing the structured drug review dataset.

The structured dataset contains patient drug reviews and ratings. It will be used for supervised machine learning to predict drug rating or effectiveness class from review text.

## Source Dataset Columns

Original dataset columns:

- uniqueID
- drugName
- condition
- review
- rating
- date
- usefulCount

## Main Table: drug_reviews

| Column Name | Data Type | Description |
|---|---|---|
| review_id | INTEGER PRIMARY KEY | Original uniqueID from the dataset |
| drug_name | TEXT | Name of the drug |
| condition | TEXT | Medical condition associated with the review |
| review_text | TEXT | Patient review text |
| rating | INTEGER | Original rating from 1 to 10 |
| review_date | DATE | Date when the review was posted |
| useful_count | INTEGER | Number of users who found the review useful |
| review_length | INTEGER | Number of characters in the review |
| review_word_count | INTEGER | Number of words in the review |
| effectiveness_class | TEXT | Derived class: low, medium, or high |

## Effectiveness Class Mapping

| Rating Range | Effectiveness Class |
|---|---|
| 1–4 | low |
| 5–7 | medium |
| 8–10 | high |

## Target Column for ML

Initial target:

```text
effectiveness_class

