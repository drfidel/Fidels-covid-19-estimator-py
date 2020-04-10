def estimator(data):
		input_data = {
		"region": {
		"name": "Africa",
		"avgAge": 19.7,
		"avgDailyIncomeInUSD": 5,
		"avgDailyIncomePopulation": 0.71
		},
		"periodType": "days",
		"timeToElapse": 58,
		"reportedCases": 674,
		"population": 66622705,
		"totalHospitalBeds": 1380614
		}

		output_data = {
		"data":input_data, 
		"impact": {
			"currentlyInfected": input_data["reportedCases"]*10,
			"infectionsByRequestedTime": input_data["currentlyInfected"]*1024
			}, 
	
		"severeImpact": {
			"currentlyInfected": input_data["reportedCases"]*10,
			"infectionsByRequestedTime": input_data["currentlyInfected"]*1024
			}
		}
		return output_data