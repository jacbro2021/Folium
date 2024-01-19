//
//  SearchViewModel.swift
//  Folium
//
//  Created by jacob brown on 1/19/24.
//

import Foundation

// MARK: Enum to hold the loading state for the search module.
enum SearchLoadingState {
    case idle
    case loading
    case success(plantList: PlantSearchList)
    case error(err: String)
}

class SearchViewModel: ObservableObject {
    
    // Published variable used to configure the search.
    @Published var speciesName: String = ""
    // Published variable used to store the current loading state for the search module.
    @Published var loadingState: SearchLoadingState = .idle

    init() {
        loadingState = .success(plantList: self.TestPlants())
    }
    
    func searchPlants() {
        // TODO: 
    }
    
    func TestPlants() -> PlantSearchList {
        return PlantSearchList(plants: [
            PlantSearchResult(id: 0,
                              commonName: "Cactus",
                              scientificName: ["Cacti"],
                              otherName: [],
                              cycle: "Perunial",
                              watering: "Frequent",
                              sunlight: ["Full Sunlight"],
                              defaultImage: PlantImage(imageID: 0,
                                                       license: 0,
                                                       licenseName: "",
                                                       licenseURL: "",
                                                       originalURL: "https://cdn.atwilltech.com/flowerdatabase/s/snake-plant-house-plant-PL112722.425.jpg",
                                                       regularURL: "",
                                                       mediumURL: "",
                                                       smallURL: "",
                                                       thumbnail: "")),
            
            PlantSearchResult(id: 1,
                              commonName: "Cactus",
                              scientificName: ["Cacti"],
                              otherName: [],
                              cycle: "Perunial",
                              watering: "Frequent",
                              sunlight: ["Full Sunlight"],
                              defaultImage: PlantImage(imageID: 0,
                                                       license: 0,
                                                       licenseName: "",
                                                       licenseURL: "",
                                                       originalURL: "https://cdn.atwilltech.com/flowerdatabase/s/snake-plant-house-plant-PL112722.425.jpg",
                                                       regularURL: "",
                                                       mediumURL: "",
                                                       smallURL: "",
                                                       thumbnail: "")),
            
            PlantSearchResult(id: 2,
                              commonName: "Cactus",
                              scientificName: [],
                              otherName: [],
                              cycle: "Perunial",
                              watering: "Frequent",
                              sunlight: ["Full Sunlight"],
                              defaultImage: PlantImage(imageID: 0,
                                                       license: 0,
                                                       licenseName: "",
                                                       licenseURL: "",
                                                       originalURL: "https://cdn.atwilltech.com/flowerdatabase/s/snake-plant-house-plant-PL112722.425.jpg",
                                                       regularURL: "",
                                                       mediumURL: "",
                                                       smallURL: "",
                                                       thumbnail: "")),
        ])
    }
}
