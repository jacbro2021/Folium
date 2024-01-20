//
//  PlantDetailViewModel.swift
//  Folium
//
//  Created by jacob brown on 1/19/24.
//

import Foundation

enum PlantDetailLoadingState {
    case idle
    case loading
    case success(plant: PlantDetails)
    case error(err: String)
}

@MainActor
class PlantDetailViewModel: ObservableObject {
    // Published var to hold the Plant Detail module's loading state.
    @Published var loadingState = PlantDetailLoadingState.idle
    
    func getPlantDetails() {
        
    }
}
