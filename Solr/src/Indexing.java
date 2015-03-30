
import java.io.IOException;
import java.net.MalformedURLException;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Types;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;

import org.apache.solr.client.solrj.SolrServerException;
import org.apache.solr.client.solrj.impl.HttpSolrServer;
import org.apache.solr.common.SolrInputDocument;

import java.sql.ResultSet;
public class Indexing {
	private static String url = "http://localhost:7574/solr/gettingstarted_shard1_replica1/";
    private static HttpSolrServer solrCore;

    
    /**
     * Creates an instance of solr 
     * 
     * @throws MalformedURLException
     */
    public Indexing() throws MalformedURLException
    {
         solrCore = new HttpSolrServer(url);
    }
    
    public void addResultSet(ResultSet rs) throws SQLException,SolrServerException, IOException
    {
     int innerCount = 0;
     Collection<SolrInputDocument> docList = new ArrayList<SolrInputDocument>();
     ResultSetMetaData rsm = rs.getMetaData();
     int numColumns = rsm.getColumnCount();
     String[] colNames = new String[numColumns + 1];

     /**
      * JDBC numbers the columns starting at 1, so the normal java convention
      * of starting at zero won't work.
      */
     for (int i = 1; i < (numColumns + 1); i++)
     {
    	 colNames[i] = rsm.getColumnName(i);           
     }

     while (rs.next())
     {
    //count++;
     innerCount++;
    SolrInputDocument doc = new SolrInputDocument();
    

    for (int j = 1; j < (numColumns + 1); j++)
    {
        if (colNames[j] != null)
        {
            Object f;
            switch (rsm.getColumnType(j))
            {
                case Types.BIGINT:
                {
                    f = rs.getLong(j);
                    break;
                }
                case Types.INTEGER:
                {
                    f = rs.getInt(j);
                    break;
                }
                case Types.DATE:
                {
                    f = rs.getDate(j);
                    break;
                }
                case Types.FLOAT:
                {
                    f = rs.getFloat(j);
                    break;
                }
                case Types.DOUBLE:
                {
                    f = rs.getDouble(j);
                    break;
                }
                case Types.TIME:
                {
                    f = rs.getDate(j);
                    break;
                }
                case Types.BOOLEAN:
                {
                    f = rs.getBoolean(j);
                    break;
                }
                default:
                {
                    f = rs.getString(j);
                }
            }
   
             doc.addField(colNames[j], f);
            }       
    }
  
 //Add document to collection
 docList.add(doc); 
}
//Add the collection to solr
solrCore.add(docList);
//Commit changes to solr
solrCore.commit();
System.out.println(innerCount+" Documents added to collection.");
}

   public static void main(String args[])
   {
	try {  		  
  		MySQLAccess s= new MySQLAccess();
  	  	Indexing indexSqlRecords=new Indexing();
  	  	ResultSet rs;
  		rs=s.readDataBase();
  		indexSqlRecords.addResultSet(rs); 
  		
  		s.close();
  	  } catch (Exception e)
	    {
  		 e.getMessage();
  		 e.printStackTrace();
  	}
   }
	
	
	

}
