import marimo

__generated_with = "0.22.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:50px;" src="mushroom.png" width=300><br>
    ## Warmup Exercise for Week 6

    For this week's warmup exercise we will be create a model to determine whether a mushroom is edible or not.

    **Dataset:** mushroom.csv (provided)

    Attribute Information:
    |Column Name | Data Values|
    |------ |------|
    |classification:|edible=e, poisonous=p|
    |cap-shape|bell=b,conical=c,convex=x,flat=f,knobbed=k,sunken=s|
    |cap-surface|fibrous=f,grooves=g,scaly=y,smooth=s|
    |cap-color|brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y|
    |bruises|bruises=t,no=f|
    |odor|almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s|
    |gill-attachment|attached=a,descending=d,free=f,notched=n|
    |gill-spacing|close=c,crowded=w,distant=d|
    |gill-size|broad=b,narrow=n|
    |gill-color|black=k,brown=n,buff=b,chocolate=h,gray=g,green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y|
    |stalk-shape|enlarging=e,tapering=t|
    |stalk-root|bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?|
    |stalk-surface-above-ring|fibrous=f,scaly=y,silky=k,smooth=s|
    |stalk-surface-below-ring|fibrous=f,scaly=y,silky=k,smooth=s|
    |stalk-color-above-ring|brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y|
    |stalk-color-below-ring|brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y|
    |veil-type| partial=p,universal=u|
    |veil-color|brown=n,orange=o,white=w,yellow=y|
    |ring-number|none=n,one=o,two=t|
    |ring-type|cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z|
    |spore-print-color|black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y|
    |population|abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y|
    |habitat|grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d|

    Missing Attribute Values: column stalk-root contains unknown values and they are denoted by "?".
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise

    The National Park Service has asked you to build a KNN model that they can use to determine in a mobile app that will help park visitors determine if a mushroom is edible or not.

    **Part 1:** <br>
     - Determine how to handle the missing values in the dataset.
     - Model the data as follows:
        * Test for the optimal number of neighbors?
        * Is it different than 2? If so, why do you think that might be? Afterall, a mushroom is either safe to eat or not safe to eat.
      - Construct a KNN model with k=2 and determine it's accuracy.

    **Part2:** <br>
       - Retrain the model without splitting the dataset into training/test for 2 neighbors
           * One way to do this is to use X in place of train_X and y instead of train_y
       - I have provided you with a dataset to test your model to use as predictions for this newer model.
           * Hint: use predict() for your second model and supply the data from the test dataset (test_data.csv)
           * Save your results, this is what you will present during the group readouts.
    """)
    return


if __name__ == "__main__":
    app.run()
