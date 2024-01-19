//
//  HomeView.swift
//  Folium
//
//  Created by jacob brown on 1/7/24.
//

import SwiftUI

struct HomeView: View {
    
    @StateObject private var vm = HomeViewModel()
    
    var body: some View {
        NavigationStack {
            VStack {
                if vm.plants.isEmpty {
                    blankView
                } else {
                    Text("Hello world")
                }
            }
            .toolbar {
                ToolbarItem(placement: .navigationBarLeading) {
                    Image("logo")
                }
                
                ToolbarItem(placement: .navigationBarTrailing) {
                    NavigationLink {
                        SearchView()
                    } label: {
                        Image(systemName: "plus")
                    }
                    .foregroundStyle(.primary)
                }
            }
        }
    }
    
    @ViewBuilder
    var blankView: some View {
        VStack {
            Image("plant")
                .resizable()
                .scaledToFit()
                .frame(width: 200)
            
            Text("No Plants to display")
                .font(.title2)
                .padding(.vertical)
                .foregroundStyle(.secondary)
            
            Text("Click the + to add new plants")
                .font(.title3)
                .foregroundStyle(.secondary)
        }
    }
}

#Preview {
    HomeView()
}
