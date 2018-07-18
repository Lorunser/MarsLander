#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {

  // declare variables
  double m, k, x0, v0, t0, t_max, dt;

  // mass, spring constant, initial position and velocity
  m = 1;
  k = 1;
  x0 = 0;
  v0 = 1;
  t0 = 0;

  // simulation time and timestep
  t_max = 100;
  dt = 0.1;

  //initialise vectors
  int N = int((t_max - t0) / dt);
  vector<double> t_list(N), x_list(N), v_list(N);

  // set initials
  t_list[0] = t0;
  x_list[0] = x0;
  v_list[0] = v0;

  //set x[1]
  x_list[1] = x0 + v0 * dt;

  //perform verlet
  double ai;
  for (int i = 1; i < N - 1; i++) {
	  //times
	  t_list[i] = t0 + dt * i;
	  
	  //positions
	  ai = -k * x_list[i] / m;
	  x_list[i+1] = 2 * x_list[i] - x_list[i - 1] + (dt * dt) * ai;

	  //velocities
	  v_list[i] = (x_list[i + 1] - x_list[i - 1]) / (2 * dt);
  }

  //one sided estimate for vinal v
  v_list[N - 1] = (x_list[N - 1] - x_list[N - 2]) / dt;
  t_list[N - 1] = t_list[N - 2] + dt;


  // Write the trajectories to file
  ofstream fout;
  fout.open("trajectories.txt");

  if (fout)
  { // file opened successfully
	for (int i = 0; i < t_list.size(); i = i + 1) {
	  fout << t_list[i] << ' ' << x_list[i] << ' ' << v_list[i] << endl;
	}
  } 
  
  else 
  { // file did not open successfully
	cout << "Could not open trajectory file for writing" << endl;
  
  }

}
