import java.io.BufferedReader;  
import java.io.InputStreamReader;  
import java.lang.*;
  
public class wordSimGenerator{ 
    public static void main(String args[]){
        double score = getSimilarity("hate", "dislike");
    }    

    public static double getSimilarity(String word1, String word2){ 
        double similarityScore = 0.0;
        try{   
            Process pr = Runtime.getRuntime().exec("python ../word2vec_client.py " + 
                                                    word1 + " " +word2);  
            BufferedReader in = new BufferedReader(new InputStreamReader(pr.getInputStream()));  
            String result = "";
            String line = "";  
            while ((line = in.readLine()) != null) {  
                result += line;
                System.out.println(result);
            }  
            in.close();  
            pr.waitFor();  
            similarityScore = Double.parseDouble(result);
        } catch (Exception e){  
            e.printStackTrace();  
        }  
        return similarityScore;
    }    
}  