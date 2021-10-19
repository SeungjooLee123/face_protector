import java.io.File;
import java.io.FileInputStream;
import java.util.Base64;
import java.util.Base64.Encoder;
import java.io.BufferedReader;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;


public class call {
    public static void main(String[] args) throws IOException{
        String url = "https://api.imgbb.com/1/upload"; 	//URL
        String key = "d1f984f4881d4a7ff17f4f04f42aa4bf";

        /*byte[] binary = getFileBinary("C:/chosun.jfif");
        String base64data = Base64.getEncoder().encodeToString(binary);
*/

        String strBase64 = "";
        File f = new File("C:/chosun.jfif");
        if (f.exists() && f.isFile() && f.length() > 0){
            byte[] bt = new byte[(int) f.length()];
            FileInputStream fis = null;
            try {
                fis = new FileInputStream(f);
                fis.read(bt);
                strBase64 = new String(Base64.encodeBase64(bt));
    
               
    
            } catch (Exception e) {
                throw e;
               
            } finally {
                try {
                    if (fis != null) {
                        fis.close();
                    }
                } catch (IOException e) {
                } catch (Exception e) {
            }
        }
        

        String resp = postRequest(url, key, strBase64);

        System.out.println(resp);
    }

    public static String postRequest(String pURL, String pkey, String img){
        String myResult = "";

        try { 
            URL url = new URL(pURL);

            HttpURLConnection http = (HttpURLConnection) url.openConnection(); 
            
            http.setDefaultUseCaches(false);
            http.setDoInput(true); 
            http.setDoOutput(true);  
            http.setRequestMethod("POST");

            http.setRequestProperty("content-type", "application/x-www-form-urlencoded");

            StringBuffer buffer = new StringBuffer();

            buffer.append("key=").append(pkey).append(" & image=").append(img);

            OutputStreamWriter outStream = new OutputStreamWriter(http.getOutputStream(), "UTF-8");
            PrintWriter writer = new PrintWriter(outStream);
            writer.write(buffer.toString());
            writer.flush();

            InputStreamReader tmp = new InputStreamReader(http.getInputStream(), "UTF-8");
            BufferedReader reader = new BufferedReader(tmp);
            StringBuilder builder = new StringBuilder();
            String str;
            while ((str = reader.readLine()) != null) {
                builder.append(str + "\n");
            }
            myResult = builder.toString();
            return myResult;

        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
 
        return myResult;
    }

    /*public static byte[] getFileBinary(String filepath) throws IOException{
        File file = new File(filepath);
        byte[] data = new byte[(int) file.length()];
        try (FileInputStream stream = new FileInputStream(file)) {
        stream.read(data, 0, data.length);
        } catch (Throwable e) {
        e.printStackTrace();
        }
        return data;
    }*/

}
