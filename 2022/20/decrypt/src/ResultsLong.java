import java.util.ArrayList;

public class ResultsLong {
    private ArrayList<ArrayList<Long>> endData;

    //constructor
    public ResultsLong(ArrayList<ArrayList<Long>> inData){
        this.endData = inData;
    }

    //method
    private int getIdxZero(){
        int idx = 0;
        while (endData.get(idx).get(0) != 0L){
            idx++;
        }
        return(idx);
    }
    public long getResult(){
        int idxZero = getIdxZero();
        int dataLength = endData.size();

        //index of the cells in x thousands position
        int one = (1000 + idxZero) % dataLength,
            two = (2000 + idxZero) % dataLength,
            three = (3000 + idxZero) % dataLength;

        //value of the cells in x thousands position
        long oneValue = endData.get(one).get(0),
             twoValue = endData.get(two).get(0),
             threeValue = endData.get(three).get(0);

        System.out.printf("%d %d %d \n",oneValue, twoValue, threeValue);
        return (oneValue + twoValue + threeValue);
    }
}
