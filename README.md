# KGMC-Results
<h2>KGMC, Lucknow - Results</h2><br>
<ul>
  <li>
    <a href="https://www.kgmu.org/kgmu_result/get_results.php?course_id=1&exam_id=2&res_id=1111">This Website<a> gives the Mark Statement of the student upon entering Roll Number. But, this does not provide the Rank Sheet ( containing the rank secured by each student).
  </li>
  <li>
    So, I have create a Spider (ranker1.py), which can scrape each student's aggregate marks, and computes total aggregate
  </li>
</ul>
<hr>
<h3>To get Output</h3><br>
Open Command Prompt in the Root directory of the Project folder. Use following commands, get the output in the desired format :-
<ul>
  <li>
    For JSON format - <code>scrapy crawl ranker1 -o dataset_json.json</code>
  </li>
  <li>
    For CSV format - <code>scrapy crawl ranker1 -o dataset_csv.csv</code>
  </li>
</ul>
NOTE :<br>
To execute above command, you should have Scrapy and Splash installed.<br>
