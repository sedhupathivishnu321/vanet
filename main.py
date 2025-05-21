import traci

# Start SUMO simulation with TraCI
traci.start(["sumo", "-c", "simulation.sumocfg"])

# Change vehicle appearance by changing its type dynamically
vehicle_id = "vehicle1"
new_vehicle_type = "bus"
traci.vehicle.setType(vehicle_id, new_vehicle_type)

# Run the simulation
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

# Close the connection
traci.close()
