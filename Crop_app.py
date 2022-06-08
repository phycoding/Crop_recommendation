import streamlit as st 
import tensorflow as tf
import numpy as np
import pandas as pd



fertilizer_dic = {
        'NHigh': """The N value of soil is high and might give rise to weeds.
        <br/> Please consider the following suggestions:
        <br/><br/> 1. <i> Manure </i> – adding manure is one of the simplest ways to amend your soil with nitrogen. Be careful as there are various types of manures with varying degrees of nitrogen.
        <br/> 2. <i>Coffee grinds </i> – use your morning addiction to feed your gardening habit! Coffee grinds are considered a green compost material which is rich in nitrogen. Once the grounds break down, your soil will be fed with delicious, delicious nitrogen. An added benefit to including coffee grounds to your soil is while it will compost, it will also help provide increased drainage to your soil.
        <br/>3. <i>Plant nitrogen fixing plants</i> – planting vegetables that are in Fabaceae family like peas, beans and soybeans have the ability to increase nitrogen in your soil
        <br/>4. Plant ‘green manure’ crops like cabbage, corn and brocolli
        <br/>5. <i>Use mulch (wet grass) while growing crops</i> - Mulch can also include sawdust and scrap soft woods""",

        'Nlow': """The N value of your soil is low.
        <br/> Please consider the following suggestions:
        <br/><br/> 1. <i>Add sawdust or fine woodchips to your soil</i> – the carbon in the sawdust/woodchips love nitrogen and will help absorb and soak up and excess nitrogen.
        <br/>2. <i>Plant heavy nitrogen feeding plants</i> – tomatoes, corn, broccoli, cabbage and spinach are examples of plants that thrive off nitrogen and will suck the nitrogen dry.
        <br/>3. <i>Water</i> – soaking your soil with water will help leach the nitrogen deeper into your soil, effectively leaving less for your plants to use.
        <br/>4. <i>Sugar</i> – In limited studies, it was shown that adding sugar to your soil can help potentially reduce the amount of nitrogen is your soil. Sugar is partially composed of carbon, an element which attracts and soaks up the nitrogen in the soil. This is similar concept to adding sawdust/woodchips which are high in carbon content.
        <br/>5. Add composted manure to the soil.
        <br/>6. Plant Nitrogen fixing plants like peas or beans.
        <br/>7. <i>Use NPK fertilizers with high N value.
        <br/>8. <i>Do nothing</i> – It may seem counter-intuitive, but if you already have plants that are producing lots of foliage, it may be best to let them continue to absorb all the nitrogen to amend the soil for your next crops.""",

        'PHigh': """The P value of your soil is high.
        <br/> Please consider the following suggestions:
        <br/><br/>1. <i>Avoid adding manure</i> – manure contains many key nutrients for your soil but typically including high levels of phosphorous. Limiting the addition of manure will help reduce phosphorus being added.
        <br/>2. <i>Use only phosphorus-free fertilizer</i> – if you can limit the amount of phosphorous added to your soil, you can let the plants use the existing phosphorus while still providing other key nutrients such as Nitrogen and Potassium. Find a fertilizer with numbers such as 10-0-10, where the zero represents no phosphorous.
        <br/>3. <i>Water your soil</i> – soaking your soil liberally will aid in driving phosphorous out of the soil. This is recommended as a last ditch effort.
        <br/>4. Plant nitrogen fixing vegetables to increase nitrogen without increasing phosphorous (like beans and peas).
        <br/>5. Use crop rotations to decrease high phosphorous levels""",

        'Plow': """The P value of your soil is low.
        <br/> Please consider the following suggestions:
        <br/><br/>1. <i>Bone meal</i> – a fast acting source that is made from ground animal bones which is rich in phosphorous.
        <br/>2. <i>Rock phosphate</i> – a slower acting source where the soil needs to convert the rock phosphate into phosphorous that the plants can use.
        <br/>3. <i>Phosphorus Fertilizers</i> – applying a fertilizer with a high phosphorous content in the NPK ratio (example: 10-20-10, 20 being phosphorous percentage).
        <br/>4. <i>Organic compost</i> – adding quality organic compost to your soil will help increase phosphorous content.
        <br/>5. <i>Manure</i> – as with compost, manure can be an excellent source of phosphorous for your plants.
        <br/>6. <i>Clay soil</i> – introducing clay particles into your soil can help retain & fix phosphorus deficiencies.
        <br/>7. <i>Ensure proper soil pH</i> – having a pH in the 6.0 to 7.0 range has been scientifically proven to have the optimal phosphorus uptake in plants.
        <br/>8. If soil pH is low, add lime or potassium carbonate to the soil as fertilizers. Pure calcium carbonate is very effective in increasing the pH value of the soil.
        <br/>9. If pH is high, addition of appreciable amount of organic matter will help acidify the soil. Application of acidifying fertilizers, such as ammonium sulfate, can help lower soil pH""",

        'KHigh': """The K value of your soil is high</b>.
        <br/> Please consider the following suggestions:
        <br/><br/>1. <i>Loosen the soil</i> deeply with a shovel, and water thoroughly to dissolve water-soluble potassium. Allow the soil to fully dry, and repeat digging and watering the soil two or three more times.
        <br/>2. <i>Sift through the soil</i>, and remove as many rocks as possible, using a soil sifter. Minerals occurring in rocks such as mica and feldspar slowly release potassium into the soil slowly through weathering.
        <br/>3. Stop applying potassium-rich commercial fertilizer. Apply only commercial fertilizer that has a '0' in the final number field. Commercial fertilizers use a three number system for measuring levels of nitrogen, phosphorous and potassium. The last number stands for potassium. Another option is to stop using commercial fertilizers all together and to begin using only organic matter to enrich the soil.
        <br/>4. Mix crushed eggshells, crushed seashells, wood ash or soft rock phosphate to the soil to add calcium. Mix in up to 10 percent of organic compost to help amend and balance the soil.
        <br/>5. Use NPK fertilizers with low K levels and organic fertilizers since they have low NPK values.
        <br/>6. Grow a cover crop of legumes that will fix nitrogen in the soil. This practice will meet the soil’s needs for nitrogen without increasing phosphorus or potassium.
        """,

        'Klow': """The K value of your soil is low.
        <br/>Please consider the following suggestions:
        <br/><br/>1. Mix in muricate of potash or sulphate of potash
        <br/>2. Try kelp meal or seaweed
        <br/>3. Try Sul-Po-Mag
        <br/>4. Bury banana peels an inch below the soils surface
        <br/>5. Use Potash fertilizers since they contain high values potassium
        """
    }
fertilizer_dic1 = {
        'NHigh': """The N value of soil is high and might give rise to weeds.
         Please consider the following suggestions:
         1.  Manure : - adding manure is one of the simplest ways to amend your soil with nitrogen. Be careful as there are various types of manures with varying degrees of nitrogen.
         2.  Coffee grinds :- use your morning addiction to feed your gardening habit! Coffee grinds are considered a green compost material which is rich in nitrogen. Once the grounds break down, your soil will be fed with delicious, delicious nitrogen. An added benefit to including coffee grounds to your soil is while it will compost, it will also help provide increased drainage to your soil.
         3.  Plant nitrogen fixing plants : - planting vegetables that are in Fabaceae family like peas, beans and soybeans have the ability to increase nitrogen in your soil
         4. Plant ‘green manure’ crops like cabbage, corn and brocolli
         5. Use mulch (wet grass) while growing crops - Mulch can also include sawdust and scrap soft woods""",

        'Nlow': """The N value of your soil is low.
         Please consider the following suggestions:
        1. Add sawdust or fine woodchips to your soil: – the carbon in the sawdust/woodchips love nitrogen and will help absorb and soak up and excess nitrogen.
        2. Plant heavy nitrogen feeding plants : – tomatoes, corn, broccoli, cabbage and spinach are examples of plants that thrive off nitrogen and will suck the nitrogen dry.
        3. <i>Water</i> – soaking your soil with water will help leach the nitrogen deeper into your soil, effectively leaving less for your plants to use.
        4. <i>Sugar</i> – In limited studies, it was shown that adding sugar to your soil can help potentially reduce the amount of nitrogen is your soil. Sugar is partially composed of carbon, an element which attracts and soaks up the nitrogen in the soil. This is similar concept to adding sawdust/woodchips which are high in carbon content.
        5. Add composted manure to the soil.
        6. Plant Nitrogen fixing plants like peas or beans.
        7. <i>Use NPK fertilizers with high N value.
        8. <i>Do nothing</i> – It may seem counter-intuitive, but if you already have plants that are producing lots of foliage, it may be best to let them continue to absorb all the nitrogen to amend the soil for your next crops.""",

        'PHigh': """The P value of your soil is high.
        Please consider the following suggestions:
        1. <i>Avoid adding manure</i> – manure contains many key nutrients for your soil but typically including high levels of phosphorous. Limiting the addition of manure will help reduce phosphorus being added.
        2. <i>Use only phosphorus-free fertilizer</i> – if you can limit the amount of phosphorous added to your soil, you can let the plants use the existing phosphorus while still providing other key nutrients such as Nitrogen and Potassium. Find a fertilizer with numbers such as 10-0-10, where the zero represents no phosphorous.
        3. <i>Water your soil</i> – soaking your soil liberally will aid in driving phosphorous out of the soil. This is recommended as a last ditch effort.
        4. Plant nitrogen fixing vegetables to increase nitrogen without increasing phosphorous (like beans and peas).
        5. Use crop rotations to decrease high phosphorous levels""",

        'Plow': """The P value of your soil is low.
        Please consider the following suggestions:
        1. <i>Bone meal</i> – a fast acting source that is made from ground animal bones which is rich in phosphorous.
        2. <i>Rock phosphate</i> – a slower acting source where the soil needs to convert the rock phosphate into phosphorous that the plants can use.
        3. <i>Phosphorus Fertilizers</i> – applying a fertilizer with a high phosphorous content in the NPK ratio (example: 10-20-10, 20 being phosphorous percentage).
        4. <i>Organic compost</i> – adding quality organic compost to your soil will help increase phosphorous content.
        5. <i>Manure</i> – as with compost, manure can be an excellent source of phosphorous for your plants.
        6. <i>Clay soil</i> – introducing clay particles into your soil can help retain & fix phosphorus deficiencies.
        7. <i>Ensure proper soil pH</i> – having a pH in the 6.0 to 7.0 range has been scientifically proven to have the optimal phosphorus uptake in plants.
        8. If soil pH is low, add lime or potassium carbonate to the soil as fertilizers. Pure calcium carbonate is very effective in increasing the pH value of the soil.
        9. If pH is high, addition of appreciable amount of organic matter will help acidify the soil. Application of acidifying fertilizers, such as ammonium sulfate, can help lower soil pH""",

        'KHigh': """The K value of your soil is high</b>.
        Please consider the following suggestions:
        1. <i>Loosen the soil</i> deeply with a shovel, and water thoroughly to dissolve water-soluble potassium. Allow the soil to fully dry, and repeat digging and watering the soil two or three more times.
        2. <i>Sift through the soil</i>, and remove as many rocks as possible, using a soil sifter. Minerals occurring in rocks such as mica and feldspar slowly release potassium into the soil slowly through weathering.
        3. Stop applying potassium-rich commercial fertilizer. Apply only commercial fertilizer that has a '0' in the final number field. Commercial fertilizers use a three number system for measuring levels of nitrogen, phosphorous and potassium. The last number stands for potassium. Another option is to stop using commercial fertilizers all together and to begin using only organic matter to enrich the soil.
        4. Mix crushed eggshells, crushed seashells, wood ash or soft rock phosphate to the soil to add calcium. Mix in up to 10 percent of organic compost to help amend and balance the soil.
        5. Use NPK fertilizers with low K levels and organic fertilizers since they have low NPK values.
        6. Grow a cover crop of legumes that will fix nitrogen in the soil. This practice will meet the soil’s needs for nitrogen without increasing phosphorus or potassium.
        """,

        'Klow': """The K value of your soil is low.
        Please consider the following suggestions:
        1. Mix in muricate of potash or sulphate of potash
        2. Try kelp meal or seaweed
        3. Try Sul-Po-Mag
        4. Bury banana peels an inch below the soils surface
        5. Use Potash fertilizers since they contain high values potassium
        """
    }



from PIL import Image
image = Image.open("cet.png")

menu=["Crop Recommendation","Fertilizer Recommendation"]
choices=st.sidebar.selectbox("Menu Bar",menu)
st.sidebar.image(image,use_column_width=True)

if choices=='Crop Recommendation':
    st.subheader("Crop Recommendation")
    #=st.selectbox("Select the overall quality(10 being 'Very Excellent' and 1 being 'very poor')",(10,9,8,7,6,5,4,3,2,1))
    N= st.number_input("Enter the value of Nitrogen",value=0,min_value=0,format='%d')
    P=st.number_input("Enter the value of Phosphorus",value=0.0,format='%f',step=1.0)
    K=st.number_input("Enter the Value of Postassium",min_value=1.0,step=1.0,format='%f')
    temperature =st.number_input("Enter Temperature",value=0.0,format='%f',step=1.0)
    humidity =st.number_input("Enter Humidity",value=0,format='%d')
    ph =st.number_input("Enter the ph value",min_value=1,max_value=10,format='%d')
    rainfall =st.number_input("Enter rainfall amount",min_value=1,max_value=10,format='%d')
    
    submit = st.button('Predict')

    
    if submit:
        st.success("Prediction Done")
        value=[N,P,K,temperature,humidity,ph,rainfall]
        df=pd.DataFrame(value).transpose()
        # st.dataframe(df)
        model= tf.keras.models.load_model("Crop_reccomandation.h5")
        clas = ('rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee')

        ans=clas[np.argmax(model.predict(df))]
        st.subheader(f"Your recommended crop is {ans} ")

if choices=='Fertilizer Recommendation':
    st.subheader("Fertilizer Recommendation")
    #=st.selectbox("Select the overall quality(10 being 'Very Excellent' and 1 being 'very poor')",(10,9,8,7,6,5,4,3,2,1))
    N= st.number_input("Enter the value of Nitrogen",value=0,min_value=0,format='%d')
    P=st.number_input("Enter the value of Phosphorus",value=0.0,format='%f',step=1.0)
    K=st.number_input("Enter the Value of Postassium",min_value=1.0,step=1.0,format='%f')
    crop = st.selectbox("Select the crop",('rice','maize','chickpea','kidneybeans','pigeonpeas','mothbeans','mungbean','blackgram','lentil','pomegranate','banana','mango','grapes','watermelon','muskmelon','apple','orange','papaya','coconut','cotton','jute','coffee'))

    
    submit = st.button('Predict')

    
    if submit:
        st.success("Prediction Done")
        df = pd.read_csv('https://raw.githubusercontent.com/Gladiator07/Harvestify/1a2ef5345f62cca8fccdbeda97cf88000895432c/Data-processed/fertilizer.csv')

        nr = df[df['Crop'] == crop]['N'].iloc[0]
        pr = df[df['Crop'] == crop]['P'].iloc[0]
        kr = df[df['Crop'] == crop]['K'].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        max_value = temp[max(temp.keys())]
        if max_value == "N":
            if n < 0:
                key = 'NHigh'
            else:
                key = "Nlow"
        elif max_value == "P":
            if p < 0:
                key = 'PHigh'
            else:
                key = "Plow"
        else:
            if k < 0:
                key = 'KHigh'
            else:
                key = "Klow"

        response = str(fertilizer_dic[key])
        st.components.v1.html(f" {response} ", width=None, height=345, scrolling=True)
        st.subheader(f" {response} ")


        
