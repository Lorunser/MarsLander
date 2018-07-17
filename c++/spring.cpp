#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {

  // declare variables
  double m, k, x, v, t_max, dt, t, a;
  vector<double> t_list, x_list, v_list;

  // mass, spring constant, initial position and velocity
  m = 1;
  k = 1;
  x = 0;
  v = 1;

  // simulation time and timestep
  t_max = 100;
  dt = 0.1;

  // Euler integration
  /*
  for (t = 0; t <= t_max; t = t + dt) {

  // append current state to trajectories
  t_list.push_back(t);
  x_list.push_back(x);
  v_list.push_back(v);

  // calculate new position and velocity
  a = -k * x / m;
  x = x + dt * v;
  v = v + dt * a;

  }
  */


  //verlet integration
  int n = 1;

  // append current state to trajectories
  t_list.push_back(t);
  x_list.push_back(x);
  v_list.push_back(v);


  for (t = dt; t <= t_max; t = t + dt) {
	  
	  //always push t
	  t_list.push_back(t);

	  if (n == 1)
	  {
		  // calculate x[1]
		  x = x + v * dt;
		  x_list.push_back(x);

		  //do not push v >> one behind always
	  }

	  else
	  {
		  //calculate a[n-1]
		  a = -k * x_list[n-1] / m;

		  //calculate v[n]
		  x = 2 * x_list[n-1] - x_list[n - 2] + (dt * dt) * a;
		  x_list.push_back(x);

		  //calculate v[n-1]
		  v = (x_list[n] - x_list[n - 2]) / (2 * dt);
		  v_list.push_back(v);
	  }

	  n++;
  }

  // one-sided estimate for final v[n]
  int N = n; // size of array
  v = (x_list[N-1] - x_list[N-2]) / dt;
  v_list.push_back(v);


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
