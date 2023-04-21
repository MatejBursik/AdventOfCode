import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/*
solution
add decryption key = 811589153
mix the cell 10 times
*/

public class MainPart2 {
    public static void main(String[] args) {
        String fileString = "";

        try {
            FileReader reader = new FileReader("input.txt");
            int txtData = reader.read();
            while (txtData != -1) {
                fileString += (char)txtData;
                txtData = reader.read();
            }
            reader.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        //making an arrayLists
        long decryption_key = 811589153L;
        ArrayList<ArrayList<Long>> fileData = new ArrayList<>();
        String line = "";
        int index = 0;
        long lindex;
        long data = 0L;
        long ddata;
        for (int i = 0; i < fileString.length(); i++){
            if (fileString.charAt(i) == '\n'){
                fileData.add(new ArrayList<Long>());
                try {
                    data = (Integer.parseInt(line.strip()));
                }
                catch (NumberFormatException e) {
                    e.printStackTrace();
                }
                ddata = data * decryption_key;
                lindex = index;
                fileData.get(index).add(0, ddata);
                fileData.get(index).add(1, lindex);
                index += 1;
                line = "";
            } else {
                line += fileString.charAt(i);
            }
        }
        System.out.println(fileData);

        //moving cells          !!ERROR!!   
        ArrayList<Long> cell;
        long distance;
        int i;
        for (int mix = 0; mix < 10; mix++) {
            for (int oi = 0; oi < fileData.size(); oi++) {
                i = 0;
                while (fileData.get(i).get(1) != oi) {
                    i++;
                }
                cell = fileData.get(i);
                distance = cell.get(0) % (fileData.size() - 1); //I assume this causes the issue

                if (distance < 0) {
                    fileData.remove(i);
                    for (int c = 0; c > distance; c--) {
                        i--;
                        if (i < 0) {
                            i = fileData.size() - 1;
                        }
                    }
                    fileData.add(i, cell);
                } else if (distance > 0) {
                    fileData.remove(i);
                    for (int c = 0; c < distance; c++) {
                        i++;
                        if (i > fileData.size() - 1) {
                            i = 0;
                        }
                    }
                    fileData.add(i, cell);
                }
            }System.out.println(fileData);
        }

        //getting the result
        ResultsLong object = new ResultsLong(fileData);
        System.out.println("The answer is: " + object.getResult());
    }
}
//too low: 2810433034
//too high:
