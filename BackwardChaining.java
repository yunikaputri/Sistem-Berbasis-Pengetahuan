import java.util.HashMap;
import java.util.Map;


public class BackwardChaining {
    public static void main(String[] args) {
    Map<String, Boolean> fakta = new HashMap<>();
    fakta.put("A", true);
    fakta.put("E", true);

    //Rule
        String[][] rules = {
                {"R1", "A B", "C"},
                {"R2", "C", "D"},
                {"R3", "A E", "F"},
                {"R4", "A", "G"},
                {"R5", "F G", "D"},
                {"R6", "G E", "H"},
                {"R7", "C H", "I"},
                {"R8", "I A", "J"},
                {"R9", "G", "J"},
                {"R10", "J", "K"},
        };

    //Menampilkan fakta awal dan fakta baru
        System.out.println("\nFakta Awal : ");
        for(Map.Entry<String, Boolean> entry : fakta.entrySet()){
            System.out.println(entry.getKey() + ":" + entry.getValue());
        }

    //penyelesaian dengan forward chaining
        boolean terbaru;
        int iterasi = 0;
        do {
            terbaru = false;
            for (String[] rule : rules){
                String premis = rule[1];
                String kesimpulan = rule[2];
                if(fakta.containsKey(premis) && !fakta.containsKey(kesimpulan)) {
                    fakta.put(kesimpulan, true);
                    terbaru = true;
                }
            }
        }while (terbaru);

        iterasi++;
        System.out.println("Iterasi " + iterasi + ": " + fakta);

    //Cek kebenaran
        if(fakta.containsKey("K") && fakta.get("K")) {
            System.out.println("K bernilai benar");
        }else {
            System.out.println("K tidak bernilai benar");
        }
    }
}