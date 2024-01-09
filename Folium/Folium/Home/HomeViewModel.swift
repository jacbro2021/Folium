//
//  HomeViewModel.swift
//  Folium
//
//  Created by jacob brown on 1/7/24.
//

import Foundation

class HomeViewModel: ObservableObject {
    
    // List of the users plants.
    // TODO: Change this to be a list of plants after creating the plant model.
    @Published var plants: [String] = []
}
