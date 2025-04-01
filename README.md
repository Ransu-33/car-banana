Software Development Tools: Car Sales Advertisement Project README

In this project, we take a look at a dataset of car sales advertisements. We're interested in factors such as the distribution of price based on the vehicles brand, and when people may start thinking about selling their car by looking at the odometer readings of the vehicles. We are also going to incorporate this data into an interactive web application so that users can make their own comparisons and conclusions.


Libraries used:

pandas
plotly.express
streamlit


Launching project:

Make sure the respective libraries are install on your system.
Open EDA.ipynb and app.py in any application that supports these files to look at EDA and code (VSCode recommended)


Launching the web app locally:

1. Open your terminal/command prompt.
2. Change the directory to where the app.py is saved.
3. Run the following command in the terminal:

streamlit run app.py

Note: You may need to change the 'vehicles_us.csv' portion of > data = pd.read_csv('vehicles_us.csv') < 
to the appropriate pathway, depending on where you download the project. For example, on Windows, the pathway might look something like:

"C:\Users\Example\Desktop\car-banana\vehicles_us.csv"

If the project is downloaded onto your desktop.


If done correctly, a local URL will show up in the terminal. It should look something like this:

Local URL: http://localhost:8501

Open the URL in your browser of choice and enjoy the project!


Project Insights:
Based off the initial findings of the web service, there are some interesting points that may be worth looking into further.

Looking at the Price of Vehicles by Days on the Market scatter plots, there seems to be a noticeable drop off in values around the 60 day mark.
Does this mean that companies aim to sell their vehicles within 2 months? Perhaps companies discount vehicles that are on their lots after a certain timeframe,
or customers may favor vehicles that haven't been on the lot for as long, if they even have access to that information.

From the Model Year Distribution histogram, most vehicles are distributed around 2011-2015. It's worth noting that there is a noticeable dip for 2009 models.
This is likely due to the recession during this time period.
