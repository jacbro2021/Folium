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

@MainActor
class SearchViewModel: ObservableObject {
    
    // Published variable used to configure the search.
    @Published var speciesName: String = ""
    // Published variable used to store the current loading state for the search module.
    @Published var loadingState: SearchLoadingState = .idle
    // Service to make calls to the Perenual API.
    private var service = SearchService()
    
    func searchPlants() {
        self.loadingState = .loading
        Task {
            do {
                self.loadingState = .success(plantList: try await service.fetchPlants(speciesName: speciesName))
            } catch {
                self.loadingState = .error(err: error.localizedDescription)
                print(error)
            }
        }
    }
}
