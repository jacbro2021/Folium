//
//  SearchView.swift
//  Folium
//
//  Created by jacob brown on 1/19/24.
//

import SwiftUI

struct SearchView: View {
    @ObservedObject var vm = SearchViewModel()

    var body: some View {
        NavigationStack {
            VStack {
                Form {
                    Section {
                        TextField("Species Name", text: $vm.speciesName)
                            .onSubmit {
                                vm.searchPlants()
                            }
                    }
                    
                    Section {
                        switch vm.loadingState {
                        case .idle:
                            ContentUnavailableView.search
                        case .loading:
                           LoadingView
                        case .success(let plantList):
                            SuccessView(plantList: plantList)
                        case .error(let err):
                            ErrorView(err: err)
                        }
                    } header: {
                        Text("Results")
                    }
                }
            }
            .navigationTitle("Plant Search")
            .navigationBarTitleDisplayMode(.large)
        }
    }
    
    @ViewBuilder private var LoadingView: some View {
        HStack {
            Spacer()
            ProgressView()
            Spacer()
        }
    }
    
    @ViewBuilder private func ErrorView(err: String) -> some View {
        HStack {
            Spacer()
            Text(err)
            Spacer()
        }
    }
    
    @ViewBuilder private func SuccessView(plantList: PlantSearchList) -> some View {
        List {
            ForEach(plantList.plants) { plant in
                NavigationLink {} label: {
                    HStack {
                        AsyncImage(url: URL(string: plant.defaultImage.originalURL)) { image in
                            image
                                .resizable()
                                .scaledToFit()
                                .frame(width: 60)
                        } placeholder: {
                            ProgressView()
                        }
                        
                        VStack(alignment: .leading) {
                            Text(plant.commonName)
                                .bold()
                                .font(.title2)
                                .padding(.vertical, 3)
                            Text(plant.scientificName.first ?? "")
                                .font(.callout)
                                .fontWeight(.thin)
                        }
                    }
                }
            }
        }
    }
}

#Preview {
    SearchView()
}
