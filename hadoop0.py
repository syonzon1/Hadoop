# -*- coding: utf-8 -*-
"""Hadoop0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FFzINDVUx4mXjTlsL8KDUIf113OYQrDS

**Install Hadoop in Google Colab**
"""

# Install java
!apt-get install openjdk-8-jdk-headless -qq > /dev/null

#create java home variable
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.0.0-bin-hadoop3.2"

"""**Step 1: Install Hadoop**"""

#download hadoop
!wget https://downloads.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz

#I use the tar command with the -x flag to extract, -z to uncompress,
#-v for verbose output, and -f to specify that we’re extracting from a file
!tar -xzvf hadoop-3.4.1.tar.gz

#copying the hadoop file to user/local
!cp -r hadoop-3.4.1/ /usr/local/

"""**Step 2: Configure java Home variable**"""

#finding  the default Java path
!readlink -f /usr/bin/java | sed "s:bin/java::"

"""**Step 3: Run Hadoop**"""

#Running Hadoop
!/usr/local/hadoop-3.4.1/bin/hadoop

!mkdir ~/input

!cp /usr/local/hadoop-3.4.1/etc/hadoop/*.xml ~/input

!ls ~/input

!/usr/local/hadoop-3.4.1/bin/hadoop jar /usr/local/hadoop-3.4.1/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar grep ~/input ~/grep_example 'allowed[.]*'

"""#Installation process: summary of the steps, problems and solutions I executed to achieve the goal

Hadoop Installation in Google Colab Hadoop is a Java-based data processing framework. In this setup, we chose to install Java within Google Colab rather than on our local machines.

**Steps Taken**
**Installing Java**

Installed OpenJDK 8 in Google Colab.

Set environment variables for Java and Spark.

**Installing Hadoop**

Downloaded Hadoop 3.4.1 from the Apache website.

Extracted the Hadoop tarball using the tar command.

Moved the extracted files to /usr/local/.

**Configuring Java Home**

Located the default Java installation path.

Set up the Java home environment variable.

**Running Hadoop**

Ran Hadoop from the Colab environment.

Created an input directory and copied necessary configuration files.

Executed a MapReduce example using the grep function.

**Challenges Faced & Solutions**
**Issue:** Slow package downloads
**Solution:** Used a stable internet connection and verified URLs before downloading.

**Issue:** Permissions error when copying files
**Solution:** Checked file ownership and used sudo if necessary.

**Issue:** Missing Java home variable
**Solution:** Verified the path using readlink -f /usr/bin/java | sed "s:bin/java::".

**Conclusion**
After successfully configuring Hadoop in Google Colab, we were able to run basic MapReduce operations. This setup provides a lightweight way to experiment with Hadoop without requiring a full local installation.

**Reference:** https://www.analyticsvidhya.com/blog/2021/05/integration-of-python-with-hadoop-and-spark/
"""
