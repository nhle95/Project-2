Project 2 (David Ma, Idean Beheshti, Travis Frocione, Nhan Le)

  Proposal: 

    Comparing GPU prices between top retailers: 

       - Best Buy

       - Microcenter
      
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
We used three sources of data for this project. First, we extracted data from Best Buy and Microcenter's websites by web scpraping using splinter. To accomplish this, we created a for loop that identifies keywords and extracts all of the GPU models and prices listed on these websites, which was then formatted into a           dictionary on Python. Lastly, we found a csv file containing a comprehensive list of GPUs and prices on Kaggle, which we read and formatted using Pandas.         
    
    Transform: explains what data clearing or transformation was required at a professional level
    
    Load: explains the final database, tables/collections, and why the topic was chosen at a professional level
    
    


