import numpy as np
import pandas as pd
def curve_fit(data):

        alpha = []
        beta = []

        d2r = np.pi/180
       
        # populate matrices
        a = range(-10, 50, 5)
        b = range(-20, 25, 5)
        for n in a:
                alpha.append(n*d2r)
        for n in b:
                beta.append(n*d2r)

        # initialize Xmat
        Xmat = [0, 0, 0, 0]
        for a in alpha:
                for b in beta:
                        val = [b, (a**2)*b, (a**2)*(b**2), (a**3)*b]
                        #print(val)
                        Xmat = np.vstack((Xmat, val))
        # delete initialization row
        Xmat = np.delete(Xmat, 0, 0)

        # organize flight data
        flight_data = []
        i = 0
        while i <= len(data)-1:
                j = 0
                while j <= len(data[0])-1:
                        flight_data.append(data[i][j])
                        j += 1
                i += 1

        # convert list to array
        # then transpose to vertical array
        flight_data = np.asarray(flight_data)
        flight_data = flight_data.T
        # get pseudo inverse
        X_pound = np.linalg.pinv(Xmat)
        # get coeffients
        coeff = np.matmul(X_pound, flight_data)
        
        #print(coeff)
        coeffT = coeff.T
        # test coefficients... very poor test
        a0 = coeff[0]
        a1 = coeff[1]
        a2 = coeff[2]
        a3 = coeff[3]

        a = -10
        b = -20
        #test = round(a0*b + a1*(a**2)*b + a2*(a**2)*(b**2) + a3*(a**3)*b,3)
        test = np.matmul(Xmat, coeffT)
      
        #print('Actual 1',data[0][0])
        print(' ')
        print('Problem 1:')
        print(' ')
        print('Data Table Computed with Coefficients:')
        print(test)
        print(' ')
        print('Coefficients', coeff)

if __name__ == "__main__":

    Data = pd.read_excel("Data/Flight_Data.xlsx")
    Data = Data.values
   
    curve_fit(Data)
