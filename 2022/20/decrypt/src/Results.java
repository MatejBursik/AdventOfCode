import java.util.ArrayList;

public class Results {
    private ArrayList<ArrayList<Integer>> endData = new ArrayList<ArrayList<Integer>>();

    //constructor
    public Results(ArrayList<ArrayList<Integer>> inData){
        this.endData = inData;
    }

    //method
    private int getIdxZero(){
        int idx = 0;
        while (endData.get(idx).get(0) != 0){
            idx++;
        }
        return(idx);
    }
    public int getResult(){
        int idxZero = getIdxZero();
        int dataLength = endData.size();

        //index of the cells in x thousands position
        int one = (1000 + idxZero) % dataLength,
            two = (2000 + idxZero) % dataLength,
            three = (3000 + idxZero) % dataLength;

        //value of the cells in x thousands position
        int oneValue = endData.get(one).get(0),
                twoValue = endData.get(two).get(0),
                threeValue = endData.get(three).get(0);

        System.out.printf("%d %d %d \n",oneValue, twoValue, threeValue);
        return (oneValue + twoValue + threeValue);
    }
}
