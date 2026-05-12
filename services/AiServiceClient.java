package services;

import org.springframework.http.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.client.SimpleClientHttpRequestFactory;

import java.util.HashMap;
import java.util.Map;

public class AiServiceClient {

    private final RestTemplate restTemplate;

    public AiServiceClient() {

        SimpleClientHttpRequestFactory factory =
                new SimpleClientHttpRequestFactory();

        factory.setConnectTimeout(10000);
        factory.setReadTimeout(10000);

        this.restTemplate = new RestTemplate(factory);
    }

    public String callDay2Validation(String text) {

        try {

            String url = "http://127.0.0.1:5001/validate";

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            Map<String, String> body = new HashMap<>();
            body.put("text", text);

            HttpEntity<Map<String, String>> request =
                    new HttpEntity<>(body, headers);

            ResponseEntity<String> response =
                    restTemplate.postForEntity(
                            url,
                            request,
                            String.class
                    );

            return response.getBody();

        } catch (Exception e) {

            System.out.println(
                    "Day2 service error: " + e.getMessage()
            );

            return null;
        }
    }

    public String callDay3Sanitizer(String text) {

        try {

            String url = "http://127.0.0.1:5002/sanitize";

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            Map<String, String> body = new HashMap<>();
            body.put("text", text);

            HttpEntity<Map<String, String>> request =
                    new HttpEntity<>(body, headers);

            ResponseEntity<String> response =
                    restTemplate.postForEntity(
                            url,
                            request,
                            String.class
                    );

            return response.getBody();

        } catch (Exception e) {

            System.out.println(
                    "Day3 service error: " + e.getMessage()
            );

            return null;
        }
    }

    public String callDay4GenerateReport() {

        try {

            String url =
                    "http://127.0.0.1:5003/generate-report";

            ResponseEntity<String> response =
                    restTemplate.postForEntity(
                            url,
                            null,
                            String.class
                    );

            return response.getBody();

        } catch (Exception e) {

            System.out.println(
                    "Day4 service error: " + e.getMessage()
            );

            return null;
        }
    }

    public String callDay5SecurityTests() {

        try {

            String url =
                    "http://127.0.0.1:5004/run-security-tests";

            ResponseEntity<String> response =
                    restTemplate.getForEntity(
                            url,
                            String.class
                    );

            return response.getBody();

        } catch (Exception e) {

            System.out.println(
                    "Day5 service error: " + e.getMessage()
            );

            return null;
        }
    }
}