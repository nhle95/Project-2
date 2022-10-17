Project 2 (David Ma, Idean Beheshti, Travis Frocione, Nhan Le)

  Proposal: 

    Comparing GPU prices between top retailers: 

       - Best Buy

       - Micro Center
      
      Sources: 
      
        https://www.kaggle.com/datasets/shilongzhuang/gpu-prices-prediction
        
            gpu_specs_prices.csv

        https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002

        https://www.microcenter.com/category/4294966937/graphics-cards
        
      Process: 

       1. Scrape and extract data from each company’s website and create two csv files.

       2. Read the csv files using Jupyter Notebook and transform it using Pandas. 

       3. Merge the csv files and load the data into a single relational database. (SQL)

       4. Determine the retailer that offers the best value for customers looking to purchase a new GPU. 


  Report:
    
    Extract: 
We used three sources of data for this project. First, we extracted data from Best Buy and Micro Center's websites by web scpraping using splinter. To accomplish this, we created a for loop that identifies keywords and extracts all of the GPU models and prices listed on these websites, which was then formatted into a           dictionary on Python. Lastly, we found a csv file containing a comprehensive list of GPUs and prices on Kaggle, which we read and formatted using Pandas.         
    
    Transform: 
For both retailers, we had to narrow down dataframe to see which listings were in the main gpu csv. For Microcenter, we filtered with keywords, filtered out any listings that didn't score higher than a 50 through fuzzy scores, and finally any duplicates/slight differences that fuzzy didnt catch. For Best Buy, we had to clean parts of the titles as some had "new!" but then did the same thing with Microcenter.
    
    Load: 
This topic was chosen to help consumers identify the retailer that provides the best value for the specific GPU that they are searching for. Our database was created in SQL using five seperate tables: gpu_kaggle, microcenter, bestbuy, microcenter_filtered, and bestbuy_filtered. The gpu_kaggle table represents the data that we extracted from the csv file. The microcenter and bestbuy tables consist of the raw data that was scraped from Micro Center and Best Buy's wesbites, while the filtered versions represent the cleaned versions. This database can be used to run queries that will allow consumers to compare each retailer's price by model name and identify the GPU that provides them with the most value. 
    
    


