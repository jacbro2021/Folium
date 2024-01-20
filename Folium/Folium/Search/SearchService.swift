//
//  SearchService.swift
//  Folium
//
//  Created by jacob brown on 1/19/24.
//

import Foundation

class SearchService {
    // Perenual API key.
    private var key: String = ""
    // Decoder for decoding json recieved from the api
    private var decoder: JSONDecoder {
        let decoder = JSONDecoder()
        // Set decoder to decode snake case naming convention.
        decoder.keyDecodingStrategy = .convertFromSnakeCase
        return decoder
    }
    // Session for making network requests
    private var session = URLSession.shared
    
    init() {
        // Get key from info.plist
        guard let infoDictionary: [String: Any] = Bundle.main.infoDictionary else { return }
        guard let apiKey = infoDictionary["PerenualAPIKey"] as? String else { return }
        self.key = apiKey
    }
    
    func fetchPlants(speciesName: String) async throws-> PlantSearchList {
        // Create URL component from url.
        guard var urlComponent = URLComponents(string: "https://perenual.com/api/species-list") else {
            fatalError("Failed to create URL component.")
        }
        
        // Add the api key to the url as a query parameter.
        urlComponent.queryItems = [
            URLQueryItem(name: "key", value: self.key),
            URLQueryItem(name: "q", value: speciesName)
        ]
        
        // Extract the url from the url component.
        guard let url = urlComponent.url else {
            fatalError("Invalid URL for fetch plantas method.")
        }
        
        // Create and configure the url request.
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        request.addValue("application/json", forHTTPHeaderField: "accept")
        
        // Make the network call and decode the response.
        let (data, _) = try await session.data(for: request)
        let plantList = try decoder.decode(PlantSearchList.self, from: data)
        
        return plantList
    }
}
