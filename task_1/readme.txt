1. Download github repository to your local machine 
2. Inside the task1 folder run cmd
3. Run the following command (in quotation marks): "docker build -t task1 ."
4. Copy local directory (path) - direcory where the github repository has been cloned 
5. Run the following command (in quotation marks): "docker run -d --name task1_doc -v <PASTE local directiory/path>:/app/config task1"

In the file named config you can change the value of the variable 'isWeatherGoodToday', possible values "true" or "false".
