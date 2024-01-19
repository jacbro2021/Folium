//
//  Perenual.swift
//  Folium
//
//  Created by jacob brown on 1/19/24.
//

import Foundation

// MARK: Models for the 'Search' feature.
struct PlantSearchList: Codable {
    let data: [PlantSearchResult]
}

struct PlantSearchResult: Codable, Identifiable {
    let id: Int
    let commonName: String
    let scientificName: [String]
    let cycle: String?
    let defaultImage: PlantImage?
}

struct PlantImage: Codable {
    let originalUrl, regularUrl, mediumUrl, smallUrl: String?
}

enum Watering: String {
    case average
    case frequent
}

// MARK: Models for the  'PlantDetails' feature/view.
struct PlantDetails {
    let id: Int
    let commonName: String
    let scientificName, otherName: [String]
    let family: NSNull
    let origin: [String]
    let type, dimension: String
    let dimensions: Dimensions
    let cycle: String
    let propagation: [String]
    let hardiness: Hardiness
    let hardinessLocation: HardinessLocation
    let watering: String
    let wateringPeriod: NSNull
    let wateringGeneralBenchmark: WateringGeneralBenchmark
    let sunlight, pruningMonth: [String]
    let seeds: Int
    let maintenance: String?
    let careGuides: String
    let soil: [String]?
    let growthRate: String
    let droughtTolerant, saltTolerant, thorny, invasive: Bool
    let tropical, indoor: Bool
    let careLevel: String
    let pestSusceptibilityAPI: String
    let flowers: Bool
    let flowerColor: String
    let cones, fruits, edibleFruit: Bool
    let edibleFruitTasteProfile, fruitNutritionalValue: String
    let harvestSeason: NSNull
    let leaf: Bool
    let leafColor: [String]
    let edibleLeaf, cuisine, medicinal: Bool
    let poisonousToHumans, poisonousToPets: Int
    let description: String
    let defaultImage: PlantImage
    let otherImages: String
}

struct Dimensions {
    let type: String
    let minValue, maxValue: Int
    let unit: String
}

struct Hardiness {
    let min, max: String
}

struct HardinessLocation {
    let fullURL: String
    let fullIframe: String
}

struct WateringGeneralBenchmark {
    let value, unit: String
}
