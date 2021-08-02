# Urobiome Microbiome Database

## Software and Tools
* AWS EC2
* [Python3](https://www.python.org/downloads/)
* [R](https://www.r-project.org/)
* Flask
* flask-sqlAlchemy

## Running Web-based DB:

#### Clone this repository:
	https://github.com/karolinasenkow/laud_demo.git
  
#### Navigate to folder containing repo:
	cd laud_demo/venv
  
#### To run:
	gunicorn run:app
  
#### In browser navigate to:
	http://ec2-3-19-27-166.us-east-2.compute.amazonaws.com/
	
## AWS EC2 Instance Setup
    
### Install
    sudo apt-get update
    sudo apt-get install nginx
    sudo apt-get install gunicorn3
#### Follow Tutorial (4:08 - 8:15):
    https://www.youtube.com/watch?v=tW6jtOOGVJI
*Note: "gunicorn app:app" should be "gunicorn run:app" since our run file is "run.py"*
  
##### Also may be useful:
    https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7

#### In case of "connection in use" error:
    sudo fuser -k {port}/tcp
    ex. sudo fuser -k 8000/tcp
    
#### MySQL Setup:
    https://likegeeks.com/mysql-on-linux-beginners-tutorial/
  
#### Virtual Environment Package Installations
    pip install flask
    pip install flask-sqlalchemy 
    pip install flask-login
    pip install flask-bcrypt
    pip install flask-wtf
    pip install mysql-connector-python
    sudo apt-get install libmysqlclient-dev
    sudo apt-get install libmariadbclient-dev
    pip3 install mysqlclient
    pip install Flask-mysqldb
    sudo apt install r-base
    pip install -U scikit-learn
    pip install seaborn
    pip install statistics
    pip install numpy
    pip install pandas
    
### Install BLAST+
    https://www.ncbi.nlm.nih.gov/books/NBK52640/
    
## File Descriptions:
#### laud_demo/venv:
* run.py : run file

#### laud_demo/venv/laud:

* blast.py
    * BLAST script
* 16S_blast_result.txt
    * txt file of blastn output against 16S db
* wgs_blast_result.txt
    * txt file of blastn output against WGS db
* assembled_contig_blast_result.txt
    * txt file of blastn output against assembled contig db
* chisq_ind.py
    * chi-squared analysis script
* t_test.E
    * T Test script
 * t_test_df.csv
     * csv file containing data that user filtered used for T Test analysis
 * two_hierarch.R
     * Two-Way Hierarchical Clustering script
 * dim_red.R
     * scripts for t-sne and PCA analysis
* dim_red_df.py
    * transform input file into correct format for analysis
* dim_df.csv
    * transformed input file that analysis is performed on
* knn.py
    * KNN script
* ML_knn_outfile.txt
    * txt file of KNN output 
* rf.py
    * Random Forest script
* ML_rf_outfile.txt
    * txt file of random forest output

#### laud_demo/venv/laud/templates
* layout.html
    * navigation bar at top of page
* about.html
    * about page
* team.html
    * team page
 * choose_query.html
     * database query page - simple sql search
 * adv_sql.html
     * custom/advanced sql search page
 * sql_example.html
     * output of sql query page
 * index.html
     * data analysis page - blast + links to other analyses
 * 16s_to_sub_id.html
     * "Check Subject ID of 16S BLAST Hit Result" page
  * chisq_ind.html
      * Chi Squared Test for Independence page
  * t_test.html
      * T Test page
 * two_hierch.html
     * Two-way Hierarchical Clustering Heatmap page
 * dim_red2.html
     * Dimensionality Reduction page - input patient file
 * dim_red.html
     * Dimensionality Reduction page - choose cure statuses, filters, etc.
  * dim_red_results.html
      * displays dimensionality reduction graph image
  * heatmap.html
      * heatmap options page - choose what to display
  * heatmap_results.html
      * displays results of heatmap
* ML.html
    * User upload / select ML algorithm page
 * RF.html
     * Random Forest page
 * knn.html
     * KNN page
* tutorial.html
    * tutorial page

#### laud_demo/venv/laud/static
* css : contains css styles
* downloads : contains empty bacterial abundance csv file which users can download to edit
* uploads : edited bacterial abundance csv file that user uploads goes here
* images : all graphs/charts that are generated during analysis are stored here
    
## Authors
Shari Tian and Karolina Senkow
