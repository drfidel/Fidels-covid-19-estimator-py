def estimator(data):
    {
	region: {
	name: "Africa",
	avgAge: 19.7,
	avgDailyIncomeInUSD: 5,
	avgDailyIncomePopulation: 0.71
	},
	periodType: "days",
	timeToElapse: 58,
	reportedCases: 674,
	population: 66622705,
	totalHospitalBeds: 1380614
	}

{
data: data, 
impact: {
	currentlyInfected = reportedCases*10
	infectionsByRequestedTime = currentlyInfected*1024
}, 
severeImpact: {
	currentlyInfected = reportedCases*10
	infectionsByRequestedTime = currentlyInfected*1024
} 
}

return data