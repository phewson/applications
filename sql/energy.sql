SELECT CASE 
         WHEN tenure::text = 'Owner occupied' THEN 'Owner occupied' 
         ELSE 'Rented' 
       END AS tenure_type,
       current_energy_efficiency, environment_impact_current, energy_consumption_current,
       co2_emissions_current, lighting_cost_current, heating_cost_current, hot_water_cost_current
FROM energy.energy_certificates 
WHERE local_authority = 'E08000033' AND tenure::text IN ('Owner occupied', 'Private Rented', 'Social Rented')  AND 
      property_type::text = 'House' AND transaction_type::text != 'new dwelling';