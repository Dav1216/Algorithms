import java.util.*;
// the traveling salesman problem
class City {
    String name;
    Map<City, Integer> adjacentCities = null;

    public City(String name) {
        this.name = name;
    }

    public void addAdjacentNodes(Map<City, Integer> adjacentCities) {
        this.adjacentCities = adjacentCities;
    }
}

public class TravelingSalesman {
    static int minCost = Integer.MAX_VALUE;
    static int counterr = 0;

    public static void main(String[] args) {
        List<City> graph = getGraph();

        List<City> visited = new ArrayList<>();
        List<City> notVisited = new ArrayList<>(graph);

        for (City city: new ArrayList<>(notVisited)) {
            notVisited.remove(city);
            visited.add(city);

            // try both {@code getMinCost} and {@code getMinCostPrune} methods.
            // One takes fewer steps than the other and the result is the same
            getMinCostPrune(visited, notVisited, 0);

            notVisited.add(city);
            visited.remove(city);
        }

        System.out.println("Counter is " + counterr);
        System.out.println("The shortest distance is " + minCost);
    }

    // the recursive method
    static void getMinCost(List<City> visited, List<City> notVisited, int sum) {
        if(notVisited.size() == 0) {
            minCost = Math.min(sum, minCost);
        }

        City lastCityGoneThrough = visited.get(visited.size() - 1);
        List<City> possibleNextVariants = notVisited.stream()
                .filter(lastCityGoneThrough.adjacentCities.keySet()::contains).toList();

        for(City nextCity: possibleNextVariants) {
            notVisited.remove(nextCity);
            visited.add(nextCity);
            getMinCost(visited, notVisited, sum + lastCityGoneThrough.adjacentCities.get(nextCity));
            counterr++;
            notVisited.add(nextCity);
            visited.remove(nextCity);
        }
    }
    // the recursive method that also prunes the search space
    static void getMinCostPrune(List<City> visited, List<City> notVisited, int sum) {
        if(notVisited.size() == 0) {
            minCost = Math.min(sum, minCost);
        }

        City lastCityGoneThrough = visited.get(visited.size() - 1);
        List<City> possibleNextVariants = notVisited.stream()
                .filter(lastCityGoneThrough.adjacentCities.keySet()::contains).toList();

        for(City nextCity: possibleNextVariants) {
            notVisited.remove(nextCity);
            visited.add(nextCity);
            if (sum + lastCityGoneThrough.adjacentCities.get(nextCity) < minCost) {
                getMinCostPrune(visited, notVisited, sum + lastCityGoneThrough.adjacentCities.get(nextCity));
                counterr++;
            }
            notVisited.add(nextCity);
            visited.remove(nextCity);
        }
    }

    static List<City> getGraph() {
        City A = new City("A");
        City B = new City("B");
        City C = new City("C");
        City D = new City("D");
        City E = new City("E");
        City F = new City("F");

        Map<City, Integer> adjA = new HashMap<>() {{ put(B, 6); put(C, 17); }};
        Map<City, Integer> adjB = new HashMap<>() {{ put(A, 6); put(D, 3); put(E, 18);}};
        Map<City, Integer> adjC = new HashMap<>() {{  put(A, 17); put(D, 15); put(F, 33);}};
        Map<City, Integer> adjD = new HashMap<>() {{ put(C, 15); put(B, 3); put(E, 25); }};
        Map<City, Integer> adjE = new HashMap<>() {{ put(F, 10); put(D, 25); put(B, 18); }};
        Map<City, Integer> adjF = new HashMap<>() {{ put(C, 33); put(E, 10);}};

        A.addAdjacentNodes(adjA);
        B.addAdjacentNodes(adjB);
        C.addAdjacentNodes(adjC);
        D.addAdjacentNodes(adjD);
        E.addAdjacentNodes(adjE);
        F.addAdjacentNodes(adjF);

        List graph = new ArrayList<>() {{add(A); add(B);add(C);add(D);add(E);add(F);}};

        return graph;
    }
}
