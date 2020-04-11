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
			"infectionsByRequestedTime": input_data["currentlyInfected"]*10*1024,
			"severeCasesByRequestedTime": input_data["reportedCases"]*10*1024*0.15,
			"hospitalBedsByRequestedTime": (input_data["reportedCases"]*10*1024*0.15)-(input_data["totalHospitalBeds"]*0.35),
			"casesForICUByRequestedTime": input_data["reportedCases"]*10*1024*0.05,
			"casesForVentilatorsByRequestedTime": input_data["reportedCases"]*10*1024*0.02,
			"dollarsInFlight": input_data["avgDailyIncomePopulation"]*input_data["avgDailyIncomeInUSD"]*(input_data["currentlyInfected"]*10*1024)*30
			}, 
	
		"severeImpact": {
			"currentlyInfected": input_data["reportedCases"]*50,
			"infectionsByRequestedTime": input_data["currentlyInfected"]*50*1024,
			"severeCasesByRequestedTime": input_data["reportedCases"]*50*1024*0.15,
			"hospitalBedsByRequestedTime": (input_data["reportedCases"]*50*1024*0.15)-(input_data["totalHospitalBeds"]*.35),
			"casesForICUByRequestedTime": input_data["reportedCases"]*50*1024*0.05,
			"casesForVentilatorsByRequestedTime": input_data["reportedCases"]*50*1024*0.02,
			"dollarsInFlight" : input_data["avgDailyIncomePopulation"]*input_data["avgDailyIncomeInUSD"]*(input_data["currentlyInfected"]*50*1024)*30
			}
		}
		return output_data