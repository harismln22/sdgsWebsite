# from pydantic import BaseModel, Field
# from bson import ObjectId
# from typing import Optional, Dict, Any


# class Data(BaseModel):
#     Agricultural_land_sq_km: Optional[float] = Field(alias="Agricultural land (sq. km)")
#     Agricultural_land_percent: Optional[float] = Field(
#         alias="Agricultural land (% of land area)"
#     )
#     Arable_land_percent: Optional[float] = Field(alias="Arable land (% of land area)")
#     Rural_land_area_below_5m_sq_km: Optional[float] = Field(
#         alias="Rural land area where elevation is below 5 meters (sq. km)"
#     )
#     Rural_land_area_below_5m_percent: Optional[float] = Field(
#         alias="Rural land area where elevation is below 5 meters (% of total land area)"
#     )
#     Urban_land_area_below_5m_sq_km: Optional[float] = Field(
#         alias="Urban land area where elevation is below 5 meters (sq. km)"
#     )
#     Urban_land_area_below_5m_percent: Optional[float] = Field(
#         alias="Urban land area where elevation is below 5 meters (% of total land area)"
#     )
#     Land_area_below_5m_percent: Optional[float] = Field(
#         alias="Land area where elevation is below 5 meters (% of total land area)"
#     )
#     Forest_area_sq_km: Optional[float] = Field(alias="Forest area (sq. km)")
#     Forest_area_percent: Optional[float] = Field(alias="Forest area (% of land area)")
#     Average_precipitation_mm_per_year: Optional[float] = Field(
#         alias="Average precipitation in depth (mm per year)"
#     )
#     Cereal_yield_kg_per_hectare: Optional[float] = Field(
#         alias="Cereal yield (kg per hectare)"
#     )
#     Access_to_electricity_percent: Optional[float] = Field(
#         alias="Access to electricity (% of population)"
#     )
#     Renewable_energy_consumption_percent: Optional[float] = Field(
#         alias="Renewable energy consumption (% of total final energy consumption)"
#     )
#     Disaster_risk_reduction_score: Optional[float] = Field(
#         alias="Disaster risk reduction progress score (1-5 scale; 5=best)"
#     )
#     Rural_population_below_5m_percent: Optional[float] = Field(
#         alias="Rural population living in areas where elevation is below 5 meters (% of total population)"
#     )
#     Urban_population_below_5m_percent: Optional[float] = Field(
#         alias="Urban population living in areas where elevation is below 5 meters (% of total population)"
#     )
#     Population_below_5m_percent: Optional[float] = Field(
#         alias="Population living in areas where elevation is below 5 meters (% of total population)"
#     )
#     Population_in_urban_agglomerations_percent: Optional[float] = Field(
#         alias="Population in urban agglomerations of more than 1 million (% of total population)"
#     )
#     Terrestrial_protected_areas_percent: Optional[float] = Field(
#         alias="Terrestrial protected areas (% of total land area)"
#     )
#     Marine_protected_areas_percent: Optional[float] = Field(
#         alias="Marine protected areas (% of territorial waters)"
#     )
#     Terrestrial_and_marine_protected_areas_percent: Optional[float] = Field(
#         alias="Terrestrial and marine protected areas (% of total territorial area)"
#     )
#     Ease_of_doing_business_rank: Optional[float] = Field(
#         alias="Ease of doing business rank (1=most business-friendly regulations)"
#     )
#     CPIA_public_sector_management_score: Optional[float] = Field(
#         alias="CPIA public sector management and institutions cluster average (1=low to 6=high)"
#     )
#     Poverty_headcount_ratio: Optional[float] = Field(
#         alias="Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)"
#     )
#     Population_growth_annual_percent: Optional[float] = Field(
#         alias="Population growth (annual %)"
#     )
#     Urban_population_growth_annual_percent: Optional[float] = Field(
#         alias="Urban population growth (annual %)"
#     )
#     Urban_population: Optional[int] = Field(alias="Urban population")
#     Urban_population_percent: Optional[float] = Field(
#         alias="Urban population (% of total population)"
#     )


# class Document(BaseModel):
#     id: Optional[str] = Field(alias="_id")
#     data: Data
#     Country_Name: str = Field(alias="Country Name")
#     Country_ISO3: str = Field(alias="Country ISO3")
#     Year: int

#     class Config:
#         allow_population_by_field_name = True
#         json_encoders = {ObjectId: str}


# class DocumentCreate(BaseModel):
#     data: Optional[Dict[str, Any]] = None
#     Country_Name: str = Field(alias="Country Name")
#     Country_ISO3: str = Field(alias="Country ISO3")
#     Year: int
