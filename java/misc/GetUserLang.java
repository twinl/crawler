package nl.sara.hadoop;

import java.io.IOException;
import java.lang.InterruptedException;
import java.io.*;

import java.util.*;
import java.util.Date;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.text.SimpleDateFormat;

import org.json.simple.*;

public class GetUserLang {
    public static void main(String args[]) {
        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
        String line = "";
        while (true) {
            try { line = stdin.readLine(); }
            catch (Throwable e) { System.out.println("Error: " + e + " " + e.getMessage()); }
            if (line == null) break;

            /* get JSON record (single line) and extract the tweet */
            Map obj = (Map) JSONValue.parse(line);
            String userlang = "unknown";
            /* process the tweet, if available */
            if (obj != null && obj.get("user") != null) {
                Map user = (Map) obj.get("user");
                if (user.get("lang") != null) { userlang = (String) user.get("lang"); }
            }
            String tweetlang = "unknown";
            if (obj != null && obj.get("lang") != null) {
                tweetlang = (String) obj.get("lang");
            }
            if (tweetlang.equals("nl")) { System.out.println(tweetlang); } 
            else { System.out.println(userlang); }
        }
    }
}
