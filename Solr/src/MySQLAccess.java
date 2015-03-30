

import java.io.Closeable;
import java.net.MalformedURLException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Date;

import org.apache.solr.client.solrj.response.QueryResponse;
public class MySQLAccess {
	
  private Connection connect = null;
  private Statement statement = null;
  private ResultSet resultSet = null;
  
  /**
   * Reads all records from the database 
   * 
   * @throws MalformedURLException
   */
  public ResultSet readDataBase() throws Exception {
    try {
    	
      //load the MySQL driver
      Class.forName("com.mysql.jdbc.Driver");
      
      //setup the connection with the the database
      connect = DriverManager.getConnection("jdbc:mysql://localhost/instagram?zeroDateTimeBehavior=convertToNull","root","");

      //statements allow to issue SQL queries to the database
      statement = connect.createStatement();
      
      //resultSet gets the result of the SQL query
      resultSet = statement.executeQuery("select * from crawleddata");
      
      //return the resultSet obtained
      return resultSet;
      
    } catch (Exception e) {
      throw e;
    }

  }

  /**
   * Closes all connections
   */
  public void close() {
   try {
	resultSet.close();
	statement.close();
	connect.close() ;
	} catch (SQLException e) {		
		e.printStackTrace();
	};   
  }
  
  } 