import numpy as np
class NN_solver:

    def __init__(self, starting_point):
        self.starting_point = starting_point
        if starting_point == 'best':
            self.starting_point = -1

    def solve(self, tsp):
        ans = np.inf
        N = tsp.N
        wanted = self.starting_point
        mat = tsp.mat
        if wanted != -1:
            visited = set(range(N))
            s = wanted
            hist = [s]
            costs = 0
            new_mat = np.copy(mat[:,:])
            visited.remove(wanted)
            while len(visited)>0:
                new_mat[:,s] = np.inf
                t = np.argmin(new_mat[s])
                hist.append(t)
                costs+=new_mat[s,t]
                visited.remove(t)
                s = t
            costs += mat[t,wanted]
            hist.append(wanted)
            ans = costs
        else:
            for i in range(N):
                visited = set(range(N))
                s = i
                hist = [s]
                costs = 0
                new_mat = np.copy(mat[:,:])
                visited.remove(i)
                while len(visited)>0:
                    new_mat[:,s] = np.inf
                    t = np.argmin(new_mat[s])
                    hist.append(t)
                    costs+=new_mat[s,t]
                    visited.remove(t)
                    s = t
                costs += mat[t,i]
                hist.append(i)
                if wanted==i:
                    return hist
                if costs < ans:
                    ans = costs
                    best_hist = hist
            hist = best_hist
        print('The cost is {}'.format(ans))
        tsp.tours['Nearest neighbor'] = hist
