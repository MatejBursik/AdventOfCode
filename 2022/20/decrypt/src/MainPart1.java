import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/*
solution
input is the entire encrypted file
the numbers determine how far they need to move
the order of their movement depends on the initial order in the file
each number moves itself once
for result look at the 1000th, 2000th, and 3000th numbers after the number with a value of 0, wrapping around the list as necessary

test case result 4, -3, 2 += = 3

plan is to create a 2d array (0=move instructions,1=original order)
make a counter for original order while relocating files
loop through the array for the next in order after every relocation
*/

public class MainPart1 {
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
        //https://www.w3schools.com/java/java_arraylist.asp
        //https://www.geeksforgeeks.org/multidimensional-collections-in-java/

        ArrayList<ArrayList<Integer>> fileData = new ArrayList<ArrayList<Integer>>();
        String line = "";
        int index = 0;
        int data = 0;
        for (int i = 0; i < fileString.length(); i++){
            if (fileString.charAt(i) == '\n'){
                fileData.add(new ArrayList<Integer>());
                try {
                    data = Integer.parseInt(line.strip());
                }
                catch (NumberFormatException e) {
                    e.printStackTrace();
                }
                fileData.get(index).add(0, data);
                fileData.get(index).add(1, index);
                index += 1;
                line = "";
            } else {
                line += fileString.charAt(i);
            }
        }
        System.out.println(fileData);
        
        //moving cells
        ArrayList<Integer> cell = new ArrayList<Integer>();
        int distance = 0;
        for (int oi = 0; oi < fileData.size(); oi++){
            int i = 0;
            while (fileData.get(i).get(1) != oi){
                i++;
            }
            cell = fileData.get(i);
            System.out.println(cell); //debug
            distance = cell.get(0) % (fileData.size()-1);

            if (distance < 0){
                fileData.remove(i);
                for (int c = 0; c > distance; c--) {i--; if(i<0){i=fileData.size()-1;}}
                fileData.add(i, cell);
            } else if (distance > 0){
                fileData.remove(i);
                for (long c = 0; c < distance; c++) {i++; if(i>fileData.size()-1){i=0;}}
                fileData.add(i, cell);
            }
            System.out.println(fileData); //debug
        }

        //getting the result
        Results object = new Results(fileData);
        System.out.println("The answer is: " + object.getResult());
    }
}
