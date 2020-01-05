# Starbucks ad campaign optimization

*Tianyi Wang*
<br>*2020 Jan 1st*

This project, from Udacity Data Scientist Nanodegree, originally was a take-home assignment provided by Starbucks. In the assignment, the result of an advertising promotion experiment is provided for us to understand what patterns in the customer features indicate that a promotion should be provided to improve not only the conversions but also the profit. The notebook in this repo provides my solution.

## Overview and Problem Statement

The background of the study is that an advertising promotion was tested to see if it would bring more customers to purchase a specific product priced at $10. Since it costs the company 0.15 to send out each promotion, it would be best to limit that promotion only to those that are most receptive to the promotion.

The data for this exercise consists of about 120,000 data points split in a 2:1 ratio among training and test files. It looks like this:

![data](https://raw.githubusercontent.com/tianyiwangnova/2020_project__Starbucks_Ad_Campaign_Optimization/master/screenshots/data_sample.png)

Each data point includes one column indicating whether or not an individual was sent a promotion for the product, and one column indicating whether or not that individual eventually purchased that product. Each individual also has seven additional features associated with them, which are provided abstractly as V1-V7.

Based on whether a customer received an ad, we can devide the customers into control group (didn't receive an ad) and experiment group (received an ad). In training data, each group has about 42k+ data points and the purchase rates are 0.76% and 1.7% for control and experiment groups. Thus we can expect that one difficult point in this project is to handle data imbalance.

![distribution](https://raw.githubusercontent.com/tianyiwangnova/2020_project__Starbucks_Ad_Campaign_Optimization/master/screenshots/train_data_description.png)

Out goal is to maximize the following metrics:
* Incremental Response Rate (IRR)
IRR depicts how many more customers purchased the product with the promotion, as compared to if they didn't receive the promotion. Mathematically, it's the ratio of the number of purchasers in the promotion group to the total number of customers in the purchasers group (treatment) minus the ratio of the number of purchasers in the non-promotional group to the total number of customers in the non-promotional group (control).
![irr](https://raw.githubusercontent.com/tianyiwangnova/2020_project__Starbucks_Ad_Campaign_Optimization/master/screenshots/irr.png)

* Net Incremental Revenue (NIR)
NIR depicts how much is made (or lost) by sending out the promotion. Mathematically, this is 10 times the total number of purchasers that received the promotion minus 0.15 times the number of promotions sent out, minus 10 times the number of purchasers who were not given the promotion.
![nir](https://raw.githubusercontent.com/tianyiwangnova/2020_project__Starbucks_Ad_Campaign_Optimization/master/screenshots/nir.png)