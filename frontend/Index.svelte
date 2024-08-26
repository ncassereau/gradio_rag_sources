<script lang="ts">

	import type { Gradio } from "@gradio/utils";
	import { Block, BlockTitle } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";

	import Arrow from "./Arrow.svelte";

	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let label = "RAG Sources";
	export let show_label = true;
	export let visible = true;
	export let value = [];
	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus;
	export let gradio: Gradio<{
		clear_status: LoadingStatus;
	}>;

	let sorted_sources = undefined;
	let sorted_by = undefined;

	function sort(keycolumn: string, order: string): void {
		function compare(a, b) {
			let key_a: number = a[keycolumn];
			let key_b: number = b[keycolumn];
			if (key_a === key_b) {
				return 0;
			}
			return (key_a < key_b) === (order === "asc") ? -1 : 1;
		}
		if (value.length === 0) {
			sorted_sources = [];
		} else {
			sorted_sources = value.sort(compare);
			sorted_by = keycolumn + order;
		}
	}

	$: value, sort("rerankScore", "desc");

</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
	{#if loading_status}
		<StatusTracker
			autoscroll={gradio.autoscroll}
			i18n={gradio.i18n}
			{...loading_status}
			on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
		/>
	{/if}

	<BlockTitle {show_label} info={undefined}>{label}</BlockTitle>

	{#if value.length > 0}
		<table class="rag-table">
			<thead>
				<tr>
					<th>URL</th>
					<th>
						<div style="display: flex; justify-content: right;">
							Retrieval Score
							<span class="arrow-grp">
								<Arrow
									direction="asc"
									height=10
									width=10
									class={sorted_by === "retrievalScoreasc" ? 'active' : ''}
									on:click={() => sort("retrievalScore", "asc")}
								/>
								<Arrow 
									direction="desc"
									height=10
									width=10
									class={sorted_by === "retrievalScoredesc" ? 'active' : ''}
									on:click={() => sort("retrievalScore", "desc")}
								/>
							</span>
						</div>
					</th>
					<th>
						<div style="display: flex; justify-content: right;">
							Rerank Score
							<span class="arrow-grp">
								<Arrow
									direction="asc"
									height=10
									width=10
									class={sorted_by === "rerankScoreasc" ? 'active' : ''}
									on:click={() => sort("rerankScore", "asc")}
								/>
								<Arrow 
									direction="desc"
									height=10
									width=10
									class={sorted_by === "rerankScoredesc" ? 'active' : ''}
									on:click={() => sort("rerankScore", "desc")}
								/>
							</span>
						</div>
					</th>
				</tr>
			</thead>
			<tbody>
				{#each sorted_sources as source}
					<tr>
						<td>
							<div style="display: flex;">
								{source.url}
								<a href="{source.url}" target="_blank" rel="noreferrer noopener" class="rag-href">
									<svg 
										height=16
										width=16
										viewBox="0 0 64 64"
										xmlns="http://www.w3.org/2000/svg"
									>
										<path d="M55.4,32V53.58a1.81,1.81,0,0,1-1.82,1.82H10.42A1.81,1.81,0,0,1,8.6,53.58V10.42A1.81,1.81,0,0,1,10.42,8.6H32"/>
										<polyline points="40.32 8.6 55.4 8.6 55.4 24.18"/>
										<line x1="19.32" y1="45.72" x2="54.61" y2="8.91"/>
									</svg>
								</a>
							</div>
						</td>
						<td style="text-align: right;">{source.retrievalScore}</td>
						<td style="text-align: right;">{source.rerankScore}</td>
					</tr>
				{/each}

			</tbody>
		</table>
	{/if}
</Block>


<style>

.rag-table {
    border-collapse: collapse;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
  	overflow: hidden;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 400px;
	width: 100%;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}
.rag-table thead tr {
    background-color: #009879;
    color: #ffffff;
    text-align: left;
}

.rag-table th,
.rag-table td {
    padding: 12px 15px;

}

.rag-table tbody tr {
    border-bottom: 1px solid #dddddd;
}


.rag-table tbody tr:last-of-type {
    border-bottom: 2px solid #009879;
}

.rag-table tbody tr:hover {
    background-color: #3e41ff;
	transition-property: background-color;
	transition-duration: 0.25s;
	transition-timing-function: ease-in-out;
}

.rag-href {
	display: inline-block;
	align-self: end;
	height: 100%;
}
.rag-href svg {
	margin-left: 5px;
	stroke-width: 3;
	stroke: var(--body-text-color);
	fill: none;
}
.rag-href svg:hover {
	stroke-width: 6px;
}

.arrow-grp {
	display: flex;
	align-items: center;
	margin-left: 5px;
}
</style>