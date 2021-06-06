# End to end Machine Learning Tutorial

<p> Welcome to the end to end supervised learning regression problem class! In this notebook (available on the Gitlab repository), we shall go through all the steps of a rather classic regression problem. The objective is to predict the sales of shops. To do this, we dispose of data from these shops (in the form of a table). Each row of our data represents a day in which the data was collected and contains the following information: </p>
<ul>
    <li> Shop_ID : shop's unique identifier. Used to know which shop we are talking about. 
    <li> Day_of_the_week : encoded from <b>0</b> to <b>6</b>.
    <li> Date : day, month and year of the data point.
    <li> Number of customers : quantity of customers that showed up that day.
    <li> Open : binary variable equal to <b>0</b> if shop closed that day and <b>1</b> if shop was open.
    <li> Promotion : binary variable equal to <b>0</b> if shop had no promotions that day and <b>1</b> if it did.
    <li> State_holiday : encoded from <b>0</b> to <b>4</b> indicating if there was a state holiday at all (<b>0</b> if not), and otherwise, the number indicates which state holiday it was.
    <li> School_holiday : Binary variable equal to <b>0</b> if there was a school holiday that day and <b>1</b> if not.
</ul>
<p> For each row, we also have the sales that the shop made on that day. We need this information in order to understand what is the relationsip between the data from the shops and the sales. Our objective today is to create a machine learning algorithm that receives information about a shop at a given day, and outputs a predicted value for the sales of the shop on that day (see Figure 1) </p>
